from copy import deepcopy
pocketDimension = {}

def getInput():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            return lines

def initializePocketDimension(lines):
    pocketDimension[0] = {}
    for y in range(len(lines)):
        pocketDimension[0][y] = {}
        for x in range(len(lines[y])):
            pocketDimension[0][y][x] = lines[y][x]
    return pocketDimension

def printPocketDimension():
    global pocketDimension
    for z in sorted(pocketDimension.keys()):
        print('\nz=' + str(z))
        for y in sorted(pocketDimension[z].keys()):
            print(''.join([pocketDimension[z][y][x] for x in sorted(pocketDimension[z][y].keys())]))

def isActive(x, y, z):
    global pocketDimension
    try:
        return pocketDimension[z][y][x] == '#'
    except:
        return False

def setActive(dimension, x, y, z):
    if not z in dimension.keys():
        dimension[z] = {}
    if not y in dimension[z].keys():
        dimension[z][y] = {}
    dimension[z][y][x] = '#'

def setInactive(dimension, x, y, z):
    if not z in dimension.keys():
        dimension[z] = {}
    if not y in dimension[z].keys():
        dimension[z][y] = {}
    dimension[z][y][x] = '.'

def get2DNeighbors(x, y, z):
    return [(z, sY, sX) for sX in [x - 1, x, x + 1] for sY in [y - 1, y, y + 1]]

def get3DNeighbors(x, y, z):
    return [coord for sZ in [z - 1, z, z + 1] for coord in get2DNeighbors(x, y, sZ) if coord != (z, y, x)]

def getActive3DNeighbors(x, y, z):
    return [coord for coord in get3DNeighbors(x, y, z) if isActive(coord[2], coord[1], coord[0])]

def expandPocketDimension():
    global pocketDimension
    newZRange = [min(pocketDimension.keys()) - 1, max(pocketDimension.keys()) + 1]
    newYRange = [min(pocketDimension[0].keys()) - 1, max(pocketDimension[0].keys()) + 1]
    newXRange = [min(pocketDimension[0][0].keys()) - 1, max(pocketDimension[0][0].keys()) + 1]
    for z in range(newZRange[0], newZRange[1] + 1):
        if not z in pocketDimension.keys():
            pocketDimension[z] = {}

        for y in range(newYRange[0], newYRange[1] + 1):
            if not y in pocketDimension[z].keys():
                pocketDimension[z][y] = {}

            for x in range(newXRange[0], newXRange[1] + 1):
                if not x in pocketDimension[z][y].keys():
                    pocketDimension[z][y][x] = '.'

def getAllCoordinatesInPocketDimension():
    global pocketDimension
    coordinates = []
    for z in pocketDimension.keys():
        for y in pocketDimension[z].keys():
            for x in pocketDimension[z][y].keys():
                coordinates.append((z, y, x))
    return coordinates
                
def cycle():
    global pocketDimension
    expandPocketDimension()
    nextPocketDimension = deepcopy(pocketDimension)
    for coordinate in getAllCoordinatesInPocketDimension():
        (z, y, x) = coordinate
        active3DNeighbors = len(getActive3DNeighbors(x, y, z))
        if isActive(x, y, z):
            if active3DNeighbors == 2 or active3DNeighbors == 3:
                setActive(nextPocketDimension, x, y, z)
            else:
                setInactive(nextPocketDimension, x, y, z)
        else:
            if active3DNeighbors == 3:
                setActive(nextPocketDimension, x, y, z)
            else:
                setInactive(nextPocketDimension, x, y, z)
    pocketDimension = nextPocketDimension

if __name__ == "__main__":
    lines = getInput()
    pocketDimension = initializePocketDimension(lines)
    for i in range(6):
        cycle()
    printPocketDimension()
    activeCubes = 0
    for coord in getAllCoordinatesInPocketDimension():
        (z, y, x) = coord
        if isActive(x, y, z):
            activeCubes += 1
    print(activeCubes)

