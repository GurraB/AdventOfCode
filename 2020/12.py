position = (0, 0)
heading = 90
waypoint = (10, 1)
directionFromDegrees = {
    0: (0, 1),
    90: (1, 0),
    180: (0, -1),
    270: (-1, 0)
}

actions = {
    'N': lambda value: ((position[0], position[1] + value), heading),
    'S': lambda value: ((position[0], position[1] - value), heading),
    'E': lambda value: ((position[0] + value, position[1]), heading),
    'W': lambda value: ((position[0] - value, position[1]), heading),
    'L': lambda value: turn(value * -1),
    'R': lambda value: turn(value),
    'F': lambda value: moveForward(value)
}

actualActions = {
    'N': lambda value: moveWayPoint(0, value),
    'S': lambda value: moveWayPoint(0, value * -1),
    'E': lambda value: moveWayPoint(value, 0),
    'W': lambda value: moveWayPoint(value * -1, 0),
    'L': lambda value: rotateLeft(value),
    'R': lambda value: rotateRight(value),
    'F': lambda value: moveForwardToWayPoint(value)
}

def moveWayPoint(stepsX, stepsY):
    global position, waypoint
    newWaypointX = waypoint[0] + stepsX
    newWaypointY = waypoint[1] + stepsY
    return (position, (newWaypointX, newWaypointY))

def rotateLeftBy90():
    global position, waypoint
    newWaypointX = waypoint[1] * -1
    newWaypointY = waypoint[0]
    return (newWaypointX, newWaypointY)

def rotateLeft(degrees):
    global waypoint
    for _ in range(degrees // 90):
        waypoint = rotateLeftBy90()
    return (position, waypoint)

def rotateRightBy90():
    global position, waypoint
    newWaypointX = waypoint[1]
    newWaypointY = waypoint[0] * -1
    return (newWaypointX, newWaypointY)

def rotateRight(degrees):
    global waypoint
    for _ in range(degrees // 90):
        waypoint = rotateRightBy90()
    return (position, waypoint)

def turn(degrees):
    global position, heading
    heading = (heading + degrees) % 360
    return position, heading

def moveForward(steps):
    global position, heading
    newX = position[0] + (steps * directionFromDegrees[heading][0])
    newY = position[1] + (steps * directionFromDegrees[heading][1])
    return ((newX, newY), heading)

def moveForwardToWayPoint(times):
    global position, waypoint
    newX = position[0] + (waypoint[0] * times)
    newY = position[1] + (waypoint[1] * times)
    return ((newX, newY), waypoint)

def getInput():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            return lines

if __name__ == "__main__":
    navigationInstructions = getInput()
    for instruction in navigationInstructions:
        print(instruction)
        (position, heading) = actions[instruction[0]](int(instruction[1:]))
        print(position)
        print(heading)
        print('----------')
    manhattanDistance = abs(position[0]) + abs(position[1])
    print(manhattanDistance)

    print('-------------------------------------------------')

    position = (0, 0)
    for instruction in navigationInstructions:
        print(instruction)
        (position, waypoint) = actualActions[instruction[0]](int(instruction[1:]))
        print(position)
        print(waypoint)
        print('----------')
    manhattanDistance = abs(position[0]) + abs(position[1])
    print(manhattanDistance)