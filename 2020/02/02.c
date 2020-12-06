#include <stdio.h>
#include <string.h>
#include <inttypes.h>

#define INPUT_SIZE 1000
#define MAX_PASSWORD_LENGTH 100

uint8_t validateSledPassword(uint8_t rangeFrom, uint8_t rangeTo, char letter, char *password) {
    uint8_t letterCount = 0;
    for (size_t i = 0; i < strlen(password); i++)
        if (password[i] == letter)
            letterCount++;
    return letterCount >= rangeFrom && letterCount <= rangeTo;
}

uint8_t validateTobogganPassword(uint8_t index1, uint8_t index2, char letter, char *password) {
    return (password[index1 - 1] == letter || password[index2 - 1] == letter) && password[index1 - 1] != password[index2 - 1];
}

int main() {
    FILE *f = fopen ("02.txt", "r");
    uint8_t range[INPUT_SIZE][2];
    char letter[INPUT_SIZE];
    char *passwords[INPUT_SIZE][MAX_PASSWORD_LENGTH];
    uint16_t counter = 0, validSledPasswords = 0, validTobogganPasswords = 0;

    while (feof(f) != 1) {
        fscanf(f, "%" PRIu8 "-%" PRIu8 " %c: %s", &range[counter][0], &range[counter][1], &letter[counter], passwords[counter]);
        counter++;
    }
    fclose(f);

    for (size_t i = 0; i < INPUT_SIZE; i++)
        if (validateSledPassword(range[i][0], range[i][1], letter[i], passwords[i]))
            validSledPasswords++;

    printf("valid sled passwords: %" PRIu16 "\n", validSledPasswords);

    for (size_t i = 0; i < INPUT_SIZE; i++)
        if (validateTobogganPassword(range[i][0], range[i][1], letter[i], passwords[i]))
            validTobogganPasswords++;

    printf("valid toboggan passwords: %" PRIu16 "\n", validTobogganPasswords);
    return 0;
}