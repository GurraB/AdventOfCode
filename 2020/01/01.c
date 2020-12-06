#include <stdio.h>
#include <inttypes.h>

#define INPUT_SIZE 200

uint8_t is2020(uint16_t num1, uint16_t num2, uint16_t num3) {
    return num1 + num2 + num3 == 2020;
}

void product(uint16_t num1, uint16_t num2, uint16_t num3, uint64_t *pRes) {
    *pRes = num1 * num2 * num3;
}

int main() {
    FILE *f = fopen ("01.txt", "r");
    uint16_t expenseReport[INPUT_SIZE];
    uint16_t counter = 0;
    uint64_t res = 0;

    while (feof(f) != 1)
        fscanf(f, "%" PRIu16, (expenseReport + counter++));
    fclose(f);

    for (size_t i = 0; i < INPUT_SIZE; i++)
    {
        for (size_t j = i + 1; j < INPUT_SIZE; j++)
        {
            if (is2020(expenseReport[i], expenseReport[j], 0))
            {
                printf("numbers: %"PRIu16 " %" PRIu16 "\n", expenseReport[i], expenseReport[j]);
                product(expenseReport[i], expenseReport[j], 1, &res);
                printf("result part 1: %" PRIu64 "\n", res);
                break;
            }
        }
        if (res)
            break;
    }
    res = 0;

    for (size_t i = 0; i < INPUT_SIZE; i++)
    {
        for (size_t j = i + 1; j < INPUT_SIZE; j++)
        {
            for (size_t k = j + 1; k < INPUT_SIZE; k++)
            {
                if (is2020(expenseReport[i], expenseReport[j], expenseReport[k]))
                {
                    printf("numbers: %"PRIu16 " %" PRIu16 " %" PRIu16 "\n", expenseReport[i], expenseReport[j], expenseReport[k]);
                    product(expenseReport[i], expenseReport[j], expenseReport[k], &res);
                    printf("result part 2: %" PRIu64 "\n", res);
                    break;
                }
            }
            if (res)
                break;
        }
        if (res)
            break;
    }
    return 0;
}