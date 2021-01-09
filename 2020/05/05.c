#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>

#define BOARDING_PASS_LENGTH 10
#define INPUT_ROWS 824

struct Seating {
    uint8_t row;
    uint8_t column;
};

uint8_t decode(char *sequence, size_t sequenceSize, uint8_t startLower, uint8_t startUpper) {
    uint8_t lower = startLower;
    uint8_t upper = startUpper;
    for (size_t i = 0; i < sequenceSize; i++)
    {
        char region = sequence[i];
        if (region == 'F' || region == 'L')
            upper = upper - ((upper - lower) / 2) - 1;
        else
            lower = lower + ((upper - lower) / 2) + 1;
    }
    return lower;
}

struct Seating decodeBoardingPass(char *boardingPass) {
    struct Seating seating = {
        .row = decode(boardingPass, 7, 0, 127),
        .column = decode(boardingPass + 7, 3, 0, 7)
    };
    return seating;
}

uint16_t getSeatId(char *boardingPass) {
    struct Seating seating = decodeBoardingPass(boardingPass);
    return seating.row * 8 + seating.column;
}

int compare (const void * a, const void * b) {
  return ( *(uint16_t*)a - *(uint16_t*)b );
}

int main() {
    FILE *f = fopen ("05.txt", "r");
    char boardingPasses[INPUT_ROWS][BOARDING_PASS_LENGTH + 1];
    uint16_t allSeats[INPUT_ROWS];
    uint16_t counter = 0;
    uint16_t mySeat, highestSeatID = 0;

    while (feof(f) != 1) {
        fscanf(f, "%s", boardingPasses[counter++]);
    }
    fclose(f);

    for (size_t i = 0; i < INPUT_ROWS; i++) {
        allSeats[i] = getSeatId(boardingPasses[i]);
        if (allSeats[i] > highestSeatID)
            highestSeatID = allSeats[i];
    }

    printf("Highest Seat ID: %" PRIu16 "\n", highestSeatID);

    qsort(allSeats, sizeof(allSeats) / sizeof(uint16_t), sizeof(uint16_t), compare);

    for (size_t i = 1; i < (sizeof(allSeats) / sizeof(uint16_t)) - 1; i++) {
        if (allSeats[i - 1] == allSeats[i] - 2 && allSeats[i + 1] == allSeats[i] + 1) {
            mySeat = allSeats[i] - 1;
            break;
        }
    }

    printf("My seat ID: %" PRIu16 "\n", mySeat);
    
    return 0;
}