#include <stdio.h>
#include <inttypes.h>
#include <string.h>
#include <stdlib.h>

#define INSTRUCTION_LENGTH 11
#define INPUT_LINES 642
#define OPERATION_LENGTH 3

enum Operation {acc, jmp, nop};

typedef struct Instruction {
    enum Operation op;
    int16_t value;
};

uint8_t parseInstruction(char *rawInstruction, struct Instruction *res) {
    struct Instruction instruction;
    char rawOperation[4];
    memcpy(rawOperation, rawInstruction, OPERATION_LENGTH);
    rawOperation[3] = '\0';
    if (strcmp(rawOperation, "acc") == 0)
        res->op = acc;
    else if (strcmp(rawOperation, "jmp") == 0)
        res->op = jmp;
    else if (strcmp(rawOperation, "nop") == 0)
        res->op = nop;
    else
        return 0;
    res->value = atoi(rawInstruction + OPERATION_LENGTH);
    return 1;
}

uint8_t instructionHasBeenVisitedBefore(uint32_t instructionIndex, uint32_t *visitedInstructions) {
    for (size_t i = 0; i < INPUT_LINES; i++)
        if (visitedInstructions[i] == instructionIndex)
            return 1;
    return 0;
}

void executeInstruction(struct Instruction instruction, int32_t *accumulator, uint32_t *programCounter) {
    if (instruction.op == nop)
        (*programCounter)++;
    else if (instruction.op == acc) {
        *accumulator += instruction.value;
        (*programCounter)++;
    } else if (instruction.op == jmp)
        *programCounter += instruction.value;
}

uint8_t executeProgram(struct Instruction *program, uint32_t programLength) {
    uint32_t visitedInstructions[INPUT_LINES] = {0};
    size_t visitedInstructionsIndex = 0;
    uint32_t programCounter = 0;
    int32_t accumulator = 0;
    visitedInstructions[visitedInstructionsIndex++] = programCounter;
    executeInstruction(program[programCounter], &accumulator, &programCounter);

    while (programCounter != programLength && !instructionHasBeenVisitedBefore(programCounter, visitedInstructions)) {
        visitedInstructions[visitedInstructionsIndex++] = programCounter;
        executeInstruction(program[programCounter], &accumulator, &programCounter);
    }
    if (programCounter == programLength) {
        printf("finished executing, accumulator: %" PRIi32 "\n", accumulator);
        return 1;
    } else {
        printf("loop at %" PRIu32 ", accumulator: %" PRIi32 "\n", programCounter, accumulator);
        return 0;
    }
}

int main() {
    FILE *f = fopen ("08.txt", "r");
    char buf[INSTRUCTION_LENGTH];
    char input[INPUT_LINES][INSTRUCTION_LENGTH];
    struct Instruction originalProgram[INPUT_LINES];
    struct Instruction modifiedProgram[INPUT_LINES];
    size_t counter = 0;
    size_t programSize = 0;
    while (fgets(buf, INSTRUCTION_LENGTH, f)) {
        strcpy(input[counter++], buf);
    }
    fclose(f);

    for (size_t i = 0; i < counter; i++)
    {
        if (parseInstruction(input[i], &originalProgram[programSize]))
            programSize++;
    }

    executeProgram(originalProgram, programSize);

    for (size_t i = 0; i < programSize; i++)
    {
        if (originalProgram[i].op == nop) {
            memcpy(modifiedProgram, originalProgram, programSize * sizeof(struct Instruction));
            modifiedProgram[i].op = jmp;
            if (executeProgram(modifiedProgram, programSize))
                break;
        } else if (originalProgram[i].op == jmp) {
            memcpy(modifiedProgram, originalProgram, programSize * sizeof(struct Instruction));
            modifiedProgram[i].op = nop;
            if (executeProgram(modifiedProgram, programSize))
                break;
        }   
    }
    
    return 0;
}