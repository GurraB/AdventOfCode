import re

def getInput():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            return lines

def formatInput(lines):
    formattedLines = []
    for line in lines:
        rangePart, charPart, password = line.split(' ')
        numberPart = [int(num) for num in re.findall('[0-9]+', rangePart)]
        letter = charPart.replace(':', '')
        formattedLines.append((numberPart, letter, password))
    return formattedLines

def validateSledPassword(validCount, letter, password):
    count = password.count(letter)
    return count >= validCount[0] and count <= validCount[1]

def validateTobogganPassword(indices, letter, password):
    pos1 = password[indices[0] - 1]
    pos2 = password[indices[1] - 1]
    return (pos1 == letter or pos2 == letter) and pos1 != pos2

if __name__ == "__main__":
    lines = getInput()
    formattedInput = formatInput(lines)
    
    validSledPasswords = 0
    for entry in formattedInput:
        if validateSledPassword(entry[0], entry[1], entry[2]):
            validSledPasswords = validSledPasswords + 1
    print(validSledPasswords)

    validTobogganPasswords = 0
    for entry in formattedInput:
        if validateTobogganPassword(entry[0], entry[1], entry[2]):
            validTobogganPasswords = validTobogganPasswords + 1
    print(validTobogganPasswords)

