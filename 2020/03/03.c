#include <stdio.h>
#include <string.h>
#include <inttypes.h>

#define SLOPE_LENGTH 323
#define SLOPE_WIDTH 31

#define ARRAY_SIZE(arr) (sizeof(arr) / sizeof(arr[0]))

struct Position
{
    uint16_t x;
    uint16_t y;
};

void getNextPosition(struct Position *pPosition, uint8_t xIncrement, uint8_t yIncrement) {
    pPosition->x += xIncrement;
    pPosition->y += yIncrement;
    if (pPosition->x >= SLOPE_WIDTH)
        pPosition->x -= SLOPE_WIDTH;
}

uint8_t reachedBottom(struct Position position) {
    return position.y >= SLOPE_LENGTH - 1;
}

int main() {
    FILE *f = fopen ("03.txt", "r");
    char slope[SLOPE_LENGTH][SLOPE_WIDTH + 1];
    struct Position currentPosition;
    currentPosition.x = 0;
    currentPosition.y = 0;
    uint8_t paths[5][2] = {
        {1, 1},
        {3, 1},
        {5, 1},
        {7, 1},
        {1, 2}
    };
    uint16_t counter = 0;
    uint16_t treeCounter[5];
    uint64_t result = 1;

    while (feof(f) != 1) {
        fscanf(f, "%s", slope[counter++]);
    }
    fclose(f);

    for (size_t i = 0; i < ARRAY_SIZE(paths); i++)
    {
        currentPosition.x = currentPosition.y = 0;
        while (!reachedBottom(currentPosition)) {
            getNextPosition(&currentPosition, paths[i][0], paths[i][1]);
            if (currentPosition.y < SLOPE_LENGTH && slope[currentPosition.y][currentPosition.x] == '#')
                treeCounter[i]++;
        }

        printf("trees hit for path (%" PRIu8 " %" PRIu8 "): %" PRIu16 "\n", paths[i][0], paths[i][1], treeCounter[i]);
        result *= treeCounter[i];
    }
    printf("result: %" PRIu64 "\n", result);
    
    return 0;
}