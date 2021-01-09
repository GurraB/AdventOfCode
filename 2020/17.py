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
    pocketDimension[0][0] = {}
    for y in range(len(lines)):
        pocketDimension[0][0][y] = {}
        for x in range(len(lines[y])):
            pocketDimension[0][0][y][x] = lines[y][x]
    return pocketDimension

def printPocketDimension():
    global pocketDimension
    for z in sorted(pocketDimension.keys()):
        print('\nz=' + str(z))
        for y in sorted(pocketDimension[z].keys()):
            print(''.join([pocketDimension[z][y][x] for x in sorted(pocketDimension[z][y].keys())]))

def isActive(x, y, z, w):
    global pocketDimension
    try:
        return pocketDimension[w][z][y][x] == '#'
    except:
        return False

def setActive(dimension, x, y, z, w):
    if not w in dimension.keys():
        dimension[w] = {}
    if not z in dimension.keys():
        dimension[w][z] = {}
    if not y in dimension[z].keys():
        dimension[w][z][y] = {}
    dimension[w][z][y][x] = '#'

def setInactive(dimension, x, y, z, w):
    if not w in dimension.keys():
        dimension[w] = {}
    if not z in dimension.keys():
        dimension[z] = {}
    if not y in dimension[z].keys():
        dimension[z][y] = {}
    dimension[w][z][y][x] = '.'

def get2DNeighbors(x, y, z, w):
    return [(w, z, sY, sX) for sX in [x - 1, x, x + 1] for sY in [y - 1, y, y + 1]]

def get3DNeighbors(x, y, z, w):
    return [coord for sZ in [z - 1, z, z + 1] for coord in get2DNeighbors(x, y, sZ, w)]

def get4DNeighbors(x, y, z, w):
    return [coord for sW in [w - 1, w, w + 1] for coord in get3DNeighbors(x, y, z, sW) if coord != (w, z, y, x)]

def getActive3DNeighbors(x, y, z, w):
    return [coord for coord in get3DNeighbors(x, y, z, w) if isActive(coord[3], coord[2], coord[1], coord[0])]

def getActive4DNeighbors(x, y, z, w):
    return [coord for coord in get4DNeighbors(x, y, z, w) if isActive(coord[3], coord[2], coord[1], coord[0])]

def expandPocketDimension():
    global pocketDimension
    newWRange = [min(pocketDimension.keys()) - 1, max(pocketDimension.keys()) + 1]
    newZRange = [min(pocketDimension[0].keys()) - 1, max(pocketDimension[0].keys()) + 1]
    newYRange = [min(pocketDimension[0][0].keys()) - 1, max(pocketDimension[0][0].keys()) + 1]
    newXRange = [min(pocketDimension[0][0][0].keys()) - 1, max(pocketDimension[0][0][0].keys()) + 1]
    for w in range(newWRange[0], newWRange[1] + 1):
        if not w in pocketDimension.keys():
            pocketDimension[w] = {}

        for z in range(newZRange[0], newZRange[1] + 1):
            if not z in pocketDimension[w].keys():
                pocketDimension[w][z] = {}

            for y in range(newYRange[0], newYRange[1] + 1):
                if not y in pocketDimension[w][z].keys():
                    pocketDimension[w][z][y] = {}

                for x in range(newXRange[0], newXRange[1] + 1):
                    if not x in pocketDimension[w][z][y].keys():
                        pocketDimension[w][z][y][x] = '.'

def getAllCoordinatesInPocketDimension():
    global pocketDimension
    coordinates = []
    for w in pocketDimension.keys():
        for z in pocketDimension[w].keys():
            for y in pocketDimension[w][z].keys():
                for x in pocketDimension[w][z][y].keys():
                    coordinates.append((w, z, y, x))
    return coordinates
                
def cycle():
    global pocketDimension
    expandPocketDimension()
    nextPocketDimension = deepcopy(pocketDimension)
    for coordinate in getAllCoordinatesInPocketDimension():
        (w, z, y, x) = coordinate
        active4DNeighbors = len(getActive4DNeighbors(x, y, z, w))
        if isActive(x, y, z, w):
            if active4DNeighbors == 2 or active4DNeighbors == 3:
                setActive(nextPocketDimension, x, y, z, w)
            else:
                setInactive(nextPocketDimension, x, y, z, w)
        else:
            if active4DNeighbors == 3:
                setActive(nextPocketDimension, x, y, z, w)
            else:
                setInactive(nextPocketDimension, x, y, z, w)
    pocketDimension = nextPocketDimension

if __name__ == "__main__":
    lines = getInput()
    pocketDimension = initializePocketDimension(lines)
    for i in range(6):
        cycle()
    #printPocketDimension()
    activeCubes = 0
    for coord in getAllCoordinatesInPocketDimension():
        (w, z, y, x) = coord
        if isActive(x, y, z, w):
            activeCubes += 1
    print(activeCubes)

