def getInput():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            return lines

def toInt(lines):
    return [int(line) for line in lines]

def isValidNumber(numbers, index, startIndex, stopIndex):
    for i in range(startIndex, stopIndex):
        for j in range(i + 1, stopIndex):
            if numbers[index] - numbers[i] - numbers[j] == 0:
                return True
    return False

def findContigiousSetResult(numbers, invalidNumber):
    for i in range(len(numbers)):
        if numbers[i] == invalidNumber:
            continue
        setValue = invalidNumber - numbers[i]
        numbersInSet = [numbers[i]]
        counter = i + 1
        while setValue > 0 and counter < len(numbers):
            setValue -= numbers[counter]
            numbersInSet.append(numbers[counter])
            if setValue == 0:
                break
            counter += 1
        if setValue == 0:
            return max(numbersInSet) + min(numbersInSet)
    return 0

if __name__ == "__main__":
    lines = getInput()
    numbers = toInt(lines)
    preamble = 25
    invalidNumber = 0
    for i in range(preamble, len(numbers)):
        if not isValidNumber(numbers, i, i - preamble, i):
            invalidNumber = numbers[i]
    print("invalidNumber:", invalidNumber)
    print("contigousSet:", findContigiousSetResult(numbers, invalidNumber))
    