accumulator = 0
programCounter = 0

operations = {
    'nop': lambda arg: (accumulator, programCounter),
    'acc': lambda arg: (accumulator + arg, programCounter),
    'jmp': lambda arg: (accumulator, programCounter + arg - 1)
}

def getInput():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            return lines

def executeProgram(program):
    global accumulator, programCounter
    accumulator = 0
    programCounter = 0
    executionMemory = []
    while True:
        if programCounter in executionMemory or programCounter >= len(program):
            break
        executionMemory.append(programCounter)
        instruction, argument = program[programCounter].split(' ')
        argument = int(argument[1:]) * -1 if argument[0] == '-' else int(argument[1:])
        (accumulator, programCounter) = operations[instruction](argument)
        programCounter = programCounter + 1
    return (accumulator, programCounter)

if __name__ == "__main__":
    program = getInput()
    for i in range(len(program)):
        if 'nop' in program[i]:
            modifiedProgram = program[:]
            modifiedProgram[i] = modifiedProgram[i].replace('nop', 'jmp')
        elif 'jmp' in program[i]:
            modifiedProgram = program[:]
            modifiedProgram[i] = modifiedProgram[i].replace('jmp', 'nop')
        else:
            continue
        (accumulator, programCounter) = executeProgram(modifiedProgram)
        if programCounter >= len(program):
            break
    print(accumulator)