def getInput():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            return lines

def findBestBus(lines):
    earliestTimestamp = int(lines[0])
    buses = [int(bus) for bus in lines[1].split(',') if bus != 'x']
    nextBusDeparture = [(bus, bus - (earliestTimestamp % bus)) for bus in buses]
    nearestDeparture = min(nextBusDeparture, key = lambda x: x[1])
    print(nearestDeparture[0] * nearestDeparture[1])

def findSubsequentBusDepartureTimestamp(lines):
    buses = [int(bus) if bus != 'x' else 1 for bus in lines[1].split(',')]
    count = buses[0]
    increment = buses[0]
    for i in range(len(buses)):
        while True:
            if (count + i) % buses[i] == 0:
                increment = 1
                for j in range(i + 1):
                    increment *= buses[j]
                break
            else:
                count += increment
    print(count)

if __name__ == "__main__":
    lines = getInput()
    findBestBus(lines)
    findSubsequentBusDepartureTimestamp(lines)