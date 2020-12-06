from functools import reduce

def getInput():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            return lines

def getNextPos(slopeMap, currPos, xIncrement, yIncrement):
    width = len(slopeMap[0])
    currX, currY = currPos
    nextX = currX + xIncrement
    nextY = currY + yIncrement
    if (nextX >= width):
        nextX = nextX - width
    return (nextX, nextY)

def isTree(slopeMap, pos):
    if (pos[1] < len(slopeMap)):
        return slopeMap[pos[1]][pos[0]] == '#'
    else:
        return False

def reachedBottom(slopeMap, pos):
    return pos[1] >= len(slopeMap) - 1

def product(*nums):
    return reduce(lambda a, b: a * b, nums)

if __name__ == "__main__":
    slopeMap = getInput()
    tobogganPaths = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    treesHitInTobogganPaths = []
    for i in range(len(tobogganPaths)):
        path = tobogganPaths[i]
        treesHitInTobogganPaths.append(0)
        currPos = (0,0)
        while(not reachedBottom(slopeMap, currPos)):
            currPos = getNextPos(slopeMap, currPos, path[0], path[1])
            if isTree(slopeMap, currPos):
                treesHitInTobogganPaths[i] = treesHitInTobogganPaths[i] + 1
        print("trees hit for path (%d, %d): %d" % (path[0], path[1], treesHitInTobogganPaths[i]))
    print("product: %d" % product(*treesHitInTobogganPaths))