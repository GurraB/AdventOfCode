#include <stdio.h>
#include <inttypes.h>
#include <string.h>

#define INPUT_ROWS 2241
#define ROW_LENGTH (28 + 1)
#define LARGEST_GROUP 12
#define NEWLINE_DELIMITER "\r\n"

void printActualString(char *str) {
    for (size_t i = 0; i < strlen(str); i++)
    {
        if (str[i] == '\0')
        {
            printf("\\0");
        } else if (str[i] == '\r')
        {
            printf("\\r");
        } else if (str[i] == '\n')
        {
            printf("\\n");
        } else
        {
            printf("%c", str[i]);
        }
    }
    printf("\n");
}

uint8_t existsInArray(char *arr, char character) {
    for (size_t i = 0; i < strlen(arr); i++)
        if (character == arr[i])
            return 1;
    return 0;
}

void addCharToSet(char *setToAddTo, char charToAdd) {
    if (!existsInArray(setToAddTo, charToAdd))
        setToAddTo[strlen(setToAddTo)] = charToAdd;
}

void addCharArrToSet(char *setToAddTo, char *charsToAdd) {
    for (size_t i = 0; i < strlen(charsToAdd); i++)
    {
        addCharToSet(setToAddTo, charsToAdd[i]);
    }
}

uint16_t uniqueYesAnswers(char *groupAnswers) {
    char uniqueAnswers[ROW_LENGTH] = {0};
    uint8_t index = 0;
    char * token = strtok(groupAnswers, NEWLINE_DELIMITER);
    while(token != NULL ) {
        addCharArrToSet(uniqueAnswers, token);
        token = strtok(NULL, NEWLINE_DELIMITER);
    }
    return strlen(uniqueAnswers);
}

void intersection(char *s1, char *s2, char *res) {
    size_t counter = 0;
    for (size_t i = 0; i < strlen(s1); i++)
    {
        for (size_t j = 0; j < strlen(s2); j++)
        {
            if (s1[i] == s2[j])
            {
                res[counter++] = s1[i];
            }
        }
    }
    res[counter] = '\0';
}

uint16_t commonYesAnswers(char *groupAnswers) {
    char commonAnswers[ROW_LENGTH] = {0};
    char temp[ROW_LENGTH] = {0};
    char * token = strtok(groupAnswers, NEWLINE_DELIMITER);
    memcpy(commonAnswers, token, strlen(token));
    token = strtok(NULL, NEWLINE_DELIMITER);
    while(token != NULL ) {
        intersection(commonAnswers, token, temp);
        if (strlen(temp) == 0)
            commonAnswers[0] = '\0';
        else
            memcpy(commonAnswers, temp, strlen(temp) + 1);
        token = strtok(NULL, NEWLINE_DELIMITER);
    }
    return strlen(commonAnswers);
}

int main() {
    FILE *f = fopen ("06.txt", "r");
    char buf[ROW_LENGTH];
    char input[INPUT_ROWS][ROW_LENGTH * LARGEST_GROUP];
    char temp[ROW_LENGTH * LARGEST_GROUP];
    size_t groupCounter = 0;
    size_t stringIndex = 0;
    
    while (fgets(buf, ROW_LENGTH, f)) {
        if (strcmp(buf, "\r\n") == 0)
        {
            groupCounter++;
            stringIndex = 0;
        } else
        {
            strcpy(input[groupCounter] + stringIndex, buf);
            stringIndex += strlen(buf);
        }
    }
    fclose(f);

    uint16_t sumOfUniqueAnswers = 0;
    uint16_t sumOfCommonAnswers = 0;
    for (size_t i = 0; i < groupCounter + 1; i++)
    {
        memcpy(temp, input[i], strlen(input[i]) + 1);
        sumOfUniqueAnswers += uniqueYesAnswers(temp);
        memcpy(temp, input[i], strlen(input[i]) + 1);
        sumOfCommonAnswers += commonYesAnswers(temp);
    }

    printf("%d\n", sumOfUniqueAnswers);
    printf("%d\n", sumOfCommonAnswers);
    return 0;
}