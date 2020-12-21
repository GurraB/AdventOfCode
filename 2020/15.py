mem = {}
turnCounter = 1

def getInput():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            return lines

def speakNumber(number):
    global mem
    if not number in mem.keys():
        mem[number] = (None, turnCounter)
    else:
        (_, turnLastSpoken) = mem[number]
        mem[number] = (turnLastSpoken, turnCounter)

def performTurn(lastNumber):
    global mem
    (turnBeforeLastSpoken, turnLastSpoken) = mem[lastNumber]
    if not turnBeforeLastSpoken is None:
        numberToSpeak = turnLastSpoken - turnBeforeLastSpoken
        speakNumber(numberToSpeak)
        return numberToSpeak
    else:
        speakNumber(0)
        return 0

def playGame(startingNumbers):
    global mem, turnCounter
    lastNumber = 0
    for n in startingNumbers:
        mem[n] = (None, turnCounter)
        turnCounter += 1
        lastNumber = n
    
    while turnCounter <= 30000000:
        lastNumber = performTurn(lastNumber)
        if turnCounter % 100000 == 0:
            print(turnCounter, lastNumber)
        turnCounter += 1

if __name__ == "__main__":
    lines = getInput()
    for line in lines:
        turnCounter = 1
        mem = {}
        playGame([int(n) for n in line.split(',')])