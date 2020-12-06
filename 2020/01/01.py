from functools import reduce

def getInput():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            return lines

def formatInput(lines):
    return [int(line) for line in lines]

def is2020(*nums):
    return sum(nums) == 2020

def product(*nums):
    return reduce(lambda a, b: a * b, nums)

if __name__ == "__main__":
    lines = getInput()
    formattedLines = formatInput(lines)

    for i in range(len(formattedLines)):
        for j in range(i + 1, len(formattedLines)):
            if is2020(formattedLines[i], formattedLines[j]):
                print(product(formattedLines[i], formattedLines[j]))

    for i in range(len(formattedLines)):
        for j in range(i + 1, len(formattedLines)):
            for k in range(j + 1, len(formattedLines)):
                if is2020(formattedLines[i], formattedLines[j], formattedLines[k]):
                    print(product(formattedLines[i], formattedLines[j], formattedLines[k]))