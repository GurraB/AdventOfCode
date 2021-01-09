#include <stdio.h>
#include <string.h>
#include <inttypes.h>
#include <stdlib.h>

#define INPUT_ROWS 1009
#define MAX_ROW_LENGTH 100
#define MAX_RAW_PASSPORT_LENGTH 200

char *allowedEyeColors[] = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"};
char *allowedHairColorChars = "0123456789abcdef";
char *allowedPassportIdChars = "0123456789";

struct Passport {
    uint16_t byr;
    uint16_t iyr;
    uint16_t eyr;
    uint16_t hgt;
    char heightUnit[3];
    char hcl[20];
    char ecl[20];
    char pid[20];
    uint8_t populatedFields;
};

int getPassportAttribute(char *rawPassport, char *attribute, char *res) {
    char *start = strstr(rawPassport, attribute);
    if (start)
    {
        char tempStr[MAX_RAW_PASSPORT_LENGTH];
        strcpy(tempStr, start);
        strcpy(res, strtok(tempStr, " \n"));
        return 1;
    }
    return 0;
}

struct Passport parsePassport(char *rawPassport) {
    struct Passport passport = {
        .populatedFields = 0
    };
    char temp[20];
    if (getPassportAttribute(rawPassport, "byr", temp)) {
        sscanf(temp, "byr:%" PRIu16, &passport.byr);
        passport.populatedFields |= 1;
    }
    if (getPassportAttribute(rawPassport, "iyr", temp)) {
        sscanf(temp, "iyr:%" PRIu16, &passport.iyr);
        passport.populatedFields |= 1 << 1;
    }
    if (getPassportAttribute(rawPassport, "eyr", temp)) {
        sscanf(temp, "eyr:%" PRIu16, &passport.eyr);
        passport.populatedFields |= 1 << 2;
    }
    if (getPassportAttribute(rawPassport, "hgt", temp)) {
        sscanf(temp, "hgt:%" PRIu16 "%s", &passport.hgt, passport.heightUnit);
        passport.populatedFields |= 1 << 3;
    }
    if (getPassportAttribute(rawPassport, "hcl", temp)) {
        sscanf(temp, "hcl:%s", passport.hcl);
        passport.populatedFields |= 1 << 4;
    }
    if (getPassportAttribute(rawPassport, "ecl", temp)) {
        sscanf(temp, "ecl:%s", passport.ecl);
        passport.populatedFields |= 1 << 5;
    }
    if (getPassportAttribute(rawPassport, "pid", temp)) {
        sscanf(temp, "pid:%s", passport.pid);
        passport.populatedFields |= 1 << 6;
    }
    return passport;
}

int passportHasRequiredFields(struct Passport *passport) {
    return (passport->populatedFields & 0b01111111) == 0b01111111;
}

int isValidLength(uint16_t length, char *unit) {
    int res = 0;
    if (strcmp(unit, "cm") == 0)
        res = length >= 150 && length <= 193;
    else
        res = length >= 59 && length <= 76;
    return res;
}

int isValidHairColor(char *hcl) {
    return strlen(hcl) == 7 && strspn(hcl, allowedHairColorChars) == 7;
}

int isValidEyeColor(char *ecl) {
    for (size_t i = 0; i < sizeof(allowedEyeColors) / sizeof(char *); i++)
    {
        if (strcmp(allowedEyeColors[i], ecl) == 0)
            return 1;
    }
    return 0;
}

int isValidPassportID(char *pid) {
    return strlen(pid) == 9 && strspn(pid, allowedPassportIdChars) == 9;
}

int isValidPassport(struct Passport *passport) {
    return (passport->byr >= 1920 && passport->byr <= 2002) &&
            (passport->iyr >= 2010 && passport->iyr <= 2020) &&
            (passport->eyr >= 2020 && passport->eyr <= 2030) &&
            isValidLength(passport->hgt, passport->heightUnit) &&
            isValidHairColor(passport->hcl) &&
            isValidEyeColor(passport->ecl) &&
            isValidPassportID(passport->pid);
}

void printPassport(struct Passport *passport) {
    printf("byr:%" PRIu16 "\niyr:%" PRIu16 "\neyr:%" PRIu16 "\nhgt:%" PRIu16 "%s\nhcl:%s\necl:%s\npid:%s\n",
        passport->byr,
        passport->iyr,
        passport->eyr,
        passport->hgt,
        passport->heightUnit,
        passport->hcl,
        passport->ecl,
        passport->pid);
}

int main() {
    FILE *f = fopen ("04.txt", "r");
    char rawPassport[MAX_RAW_PASSPORT_LENGTH];
    char **allUnparsedPassports = malloc(INPUT_ROWS * sizeof(char *));
    struct Passport passports[INPUT_ROWS] = {{.populatedFields = 0}};
    uint16_t counter = 0;
    uint16_t passportsWithRequiredFields, validPassports = 0;
    allUnparsedPassports[counter] = malloc(MAX_RAW_PASSPORT_LENGTH);

    while (feof(f) != 1) {
        fgets(rawPassport, MAX_RAW_PASSPORT_LENGTH, f);
        
        if (strlen(rawPassport) == 2) {
            counter++;
            allUnparsedPassports[counter] = malloc(MAX_RAW_PASSPORT_LENGTH);
        } else
            strcat(allUnparsedPassports[counter], rawPassport);
    }
    fclose(f);

    for (size_t i = 0; i < INPUT_ROWS; i++)
    {
        if (allUnparsedPassports[i])
            passports[i] = parsePassport(allUnparsedPassports[i]);
    }

    for (size_t i = 0; i < INPUT_ROWS; i++)
    {
        if (allUnparsedPassports[i])
            free(&allUnparsedPassports[i]);
    }

    for (size_t i = 0; i < INPUT_ROWS; i++)
    {   
        if (passportHasRequiredFields(&passports[i])) {
            passportsWithRequiredFields++;
            if (isValidPassport(&passports[i]))
                validPassports++;
        }
    }

    printf("Passports with required fields: %d\n", passportsWithRequiredFields);
    printf("Valid passports: %d\n", validPassports);
    return 0;
}