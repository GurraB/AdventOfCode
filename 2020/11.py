def getInput():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            return lines

def getImmediateSurroundingSeats(seatingArrangement, seat):
    indices = [(sY, sX) for sX in [seat[1] - 1, seat[1], seat[1] + 1] for sY in [seat[0] - 1, seat[0], seat[0] + 1] if (sY, sX) != seat]
    indices = list(filter(lambda index: \
        index[0] >= 0 and \
        index[0] < len(seatingArrangement) and \
        index[1] >= 0 and \
        index[1] < len(seatingArrangement[0]), \
        indices))
    return indices

def getNextSeatInSightIsOccupied(seatingArrangement, seat, increment):
    nextSeat = (seat[0] + increment[0], seat[1] + increment[1])
    while nextSeat[0] >= 0 and nextSeat[0] < len(seatingArrangement) and nextSeat[1] >= 0 and nextSeat[1] < len(seatingArrangement[0]):
        if isFloor(seatingArrangement, nextSeat):
            nextSeat = (nextSeat[0] + increment[0], nextSeat[1] + increment[1])
        else:
            return isOccupied(seatingArrangement, nextSeat)
    return False

def getSurroundingSeatsAreOccupied(seatingArrangement, seat):
    directions = [(sY, sX) for sX in [-1, 0, 1] for sY in [-1, 0, 1] if (sY, sX) != (0, 0)]
    isOccupiedInDirection = []
    for direction in directions:
        nextSeatInSight = getNextSeatInSightIsOccupied(seatingArrangement, seat, direction)
        if not nextSeatInSight is None:
            isOccupiedInDirection.append(nextSeatInSight)
    #print((seat), directions, isOccupiedInDirection)
    return isOccupiedInDirection

def getNextValueUsingImmediate(seatingArrangement, seat):
    if isFloor(seatingArrangement, seat):
        return '.'
    elif isEmpty(seatingArrangement, seat):
        if not True in [isOccupied(seatingArrangement, s) for s in getImmediateSurroundingSeats(seatingArrangement, seat)]:
            return '#'
    elif isOccupied(seatingArrangement, seat):
        if len(list(filter(lambda occupied: occupied, [isOccupied(seatingArrangement, s) for s in getImmediateSurroundingSeats(seatingArrangement, seat)]))) >= 4:
            return 'L'
    return seatingArrangement[seat[0]][seat[1]]

def getNextValue(seatingArrangement, seat):
    if isFloor(seatingArrangement, seat):
        return '.'
    elif isEmpty(seatingArrangement, seat):
        if not True in getSurroundingSeatsAreOccupied(seatingArrangement, seat):
            return '#'
    elif isOccupied(seatingArrangement, seat):
        if len(list(filter(lambda occupied: occupied, getSurroundingSeatsAreOccupied(seatingArrangement, seat)))) >= 5:
            return 'L'
    return seatingArrangement[seat[0]][seat[1]]

def isOccupied(seatingArrangement, seat):
    return seatingArrangement[seat[0]][seat[1]] == '#'

def isEmpty(seatingArrangement, seat):
    return seatingArrangement[seat[0]][seat[1]] == 'L'

def isFloor(seatingArrangement, seat):
    return seatingArrangement[seat[0]][seat[1]] == '.'

def getSeatingArrangement(lines):
    return [[seat for seat in line] for line in lines]

def performIterationUsingImmediate(seatingArrangement):
    newSeatingArrangement = []
    for line in seatingArrangement:
        newSeatingArrangement.append(line[:])
    for y in range(len(seatingArrangement)):
        for x in range(len(seatingArrangement[0])):
            newSeatingArrangement[y][x] = getNextValueUsingImmediate(seatingArrangement, (y, x))
    return newSeatingArrangement

def performIteration(seatingArrangement):
    newSeatingArrangement = []
    for line in seatingArrangement:
        newSeatingArrangement.append(line[:])
    for y in range(len(seatingArrangement)):
        for x in range(len(seatingArrangement[0])):
            newSeatingArrangement[y][x] = getNextValue(seatingArrangement, (y, x))
    return newSeatingArrangement

def noOfOccupiedSeats(seatingArrangement):
    count = 0
    for y in range(len(seatingArrangement)):
        for x in range(len(seatingArrangement[0])):
            if isOccupied(seatingArrangement, (y, x)):
                count += 1
    return count

if __name__ == "__main__":
    lines = getInput()
    originalSeatingArrangement = getSeatingArrangement(lines)
    seatingArrangement = originalSeatingArrangement[:]
    newSeatingArrangement = []
    while True:
        newSeatingArrangement = performIterationUsingImmediate(seatingArrangement)
        if seatingArrangement == newSeatingArrangement:
            break
        else:
            seatingArrangement = newSeatingArrangement
        #print()
        #for line in newSeatingArrangement:
        #    print(line)
    print()
    print("occupied seats:", noOfOccupiedSeats(seatingArrangement))

    seatingArrangement = originalSeatingArrangement[:]

    while True:
        newSeatingArrangement = performIteration(seatingArrangement)
        if seatingArrangement == newSeatingArrangement:
            break
        else:
            seatingArrangement = newSeatingArrangement
        #print()
        #for line in newSeatingArrangement:
        #    print(line)
    print()
    print("occupied seats:", noOfOccupiedSeats(seatingArrangement))