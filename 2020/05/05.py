def getInput():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            return lines

def decode(sequence, startLower, startUpper):
    lower = startLower
    upper = startUpper
    for region in sequence:
        if region == 'F' or region == 'L':
            upper = int(upper - ((upper - lower) / 2))
        else:
            lower = int(lower + ((upper - lower) / 2)) + 1
    return lower

def decodeBoardingPass(boardingPass):
    row = decode(boardingPass[:7], 0, 127)
    column = decode(boardingPass[7:], 0, 7)
    return row, column

def getSeatId(boardingPass):
    row, column = decodeBoardingPass(boardingPass)
    return row * 8 + column

if __name__ == "__main__":
    seatIds = [getSeatId(line) for line in getInput()]
    print("max seat ID %d" % max(seatIds))

    sortedSeats = sorted(seatIds)
    previousSeat = 53
    for i in range(len(seatIds)):
        s = int(sortedSeats[i])
        if previousSeat + 1 != s:
            print("My seat ID: %d" % (previousSeat + 1))
            break
        previousSeat = s