#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>

#define PREAMBLE_LENGTH 25
#define PREVIOUS_NUMBERS_TO_CONSIDER 25

#define INPUT_LINES 1000
#define LINE_LENGTH 20

void addNumberToCircularBuffer(uint64_t *allNumbers, size_t *pIndex, uint64_t number) {
    allNumbers[(*pIndex)++] = number;
    if (*pIndex >= PREVIOUS_NUMBERS_TO_CONSIDER)
        *pIndex = 0;
}

uint8_t isValidNumber(uint64_t *allNumbers, uint64_t number) {
    for (size_t i = 0; i < PREVIOUS_NUMBERS_TO_CONSIDER; i++)
        for (size_t j = i; j < PREVIOUS_NUMBERS_TO_CONSIDER; j++)
            if ((number - allNumbers[i] - allNumbers[j]) == 0)
                return 1;
    return 0;
}

uint8_t containsDuplicates(uint64_t *allNumbers, size_t startIndex, size_t endIndex) {
    for (size_t i = startIndex; i < endIndex; i++)
        for (size_t j = i + 1; j < endIndex; j++)
            if (allNumbers[i] == allNumbers[j])
                return 1;
    return 0;
}

uint64_t getSumOfMaxAndMinInInterval(uint64_t *allNumbers, size_t startIndex, size_t endIndex) {
    uint64_t max = 0, min = UINT64_MAX;
    for (size_t i = startIndex; i < endIndex; i++)
    {
        if (allNumbers[i] < min)
            min = allNumbers[i];
        if (allNumbers[i] > max)
            max = allNumbers[i];
    }
    return min + max;
}

uint64_t findContigousNumbers(uint64_t *allNumbers, uint64_t invalidNumber) {
    uint64_t sum = 0;
    size_t counter = 0;
    for (size_t i = 0; i < INPUT_LINES; i++)
    {
        if (allNumbers[i] == invalidNumber)
            continue;
        
        while (sum < invalidNumber && (i + counter) < INPUT_LINES) {
            sum += allNumbers[i + counter++];
        }
        if (sum == invalidNumber && !containsDuplicates(allNumbers, i, i + counter))
            return getSumOfMaxAndMinInInterval(allNumbers, i, i + counter);
        else {
            sum = 0;
            counter = 0;
        }
    }
    return 0;
}

int main() {
    FILE *f = fopen("09.txt", "r");
    char buf[LINE_LENGTH];
    uint64_t circularBuffer[PREVIOUS_NUMBERS_TO_CONSIDER];
    size_t circularBufferIndex = 0;
    size_t counter = 0;
    uint64_t currentNumber = 0;
    while (fgets(buf, LINE_LENGTH, f)) {
        if (counter++ < PREAMBLE_LENGTH)
            addNumberToCircularBuffer(circularBuffer, &circularBufferIndex, strtoull(buf, NULL, 10));
        else {
            currentNumber = strtoull(buf, NULL, 10);
            if (!isValidNumber(circularBuffer, currentNumber))
            {
                printf("invalid number: %" PRIu64 "\n", currentNumber);
                break;
            } else
                addNumberToCircularBuffer(circularBuffer, &circularBufferIndex, currentNumber);
        }
    }
    fclose(f);

    uint64_t allNumbers[INPUT_LINES];
    counter = 0;

    f = fopen("09.txt", "r");
    while (fgets(buf, LINE_LENGTH, f))
        allNumbers[counter++] = strtoull(buf, NULL, 10);
    fclose(f);

    printf("contigousNumber: %" PRIu64 "\n", findContigousNumbers(allNumbers, currentNumber));

    return 0;
}