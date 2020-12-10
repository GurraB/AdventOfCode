adapterMem = {}

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

def getCombinationsForAdapter(adapter, sortedAdapters):
    global adapterMem
    if adapter == sortedAdapters[-1]:
        return 1
    elif adapter in adapterMem.keys():
        return adapterMem[adapter]
    else:
        adapterMem[adapter] = 0
        for possibleConnection in getPossibleConnections(adapter, sortedAdapters):
            adapterMem[adapter] += getCombinationsForAdapter(possibleConnection, sortedAdapters)
        return adapterMem[adapter]

def getPossibleConnections(adapter, sortedAdapters):
    possibleConnections = []
    for i in range(len(sortedAdapters)):
        if sortedAdapters[i] <= adapter:
            continue
        if sortedAdapters[i] - adapter > 3:
            break
        possibleConnections.append(sortedAdapters[i])
    return possibleConnections

if __name__ == "__main__":
    lines = getInput()
    adapters = toInt(lines)
    sortedAdapters = sorted(adapters)
    adapterDiffs = {}
    for i in range(1, len(sortedAdapters)):
        diff = sortedAdapters[i] - sortedAdapters[i - 1]
        if diff in adapterDiffs.keys():
            adapterDiffs[diff] += 1
        else:
            adapterDiffs[diff] = 2
    print("res", adapterDiffs[1] * adapterDiffs[3])
    print(getCombinationsForAdapter(0, sortedAdapters))