import re

bagMem = {}

def getInput():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            return lines

def getSuperBags(superBags, visited, bagDescription, bagDict: dict):
    if bagDescription in visited:
        return set(superBags)
    visited.append(bagDescription)
    for key in bagDict.keys():
        for innerbag in bagDict[key]:
            if innerbag[0] == bagDescription:
                superBags.append(key)
                superBags.extend(getSuperBags(superBags, visited, key, bagDict))
    return set(superBags)
        
def getRequiredBagsInBag(bagDescription, bagDict):
    global bagMem
    if len(bagDict[bagDescription]) == 0:
        return 1
    if bagDescription in bagMem.keys():
        return bagMem[bagDescription]
    total = 1
    for bag in bagDict[bagDescription]:
        desc = bag[0]
        count = int(bag[1])
        total += getRequiredBagsInBag(desc, bagDict) * count
    bagMem[bagDescription] = total
    return total


def parseBag(bag: str):
    importantWords = ''.join([word for word in bag.split() if word.lower() not in ['bag', 'bags', 'bag,', 'bags,', 'bag.', 'bags.', 'contain', 'no', 'other']])
    bagDescription = re.split(r'(\d+)', importantWords)
    outerBag = bagDescription[0]
    innerBags = []
    for i in range(1, len(bagDescription), 2):
        count = bagDescription[i]
        desc = bagDescription[i + 1]
        innerBags.append((desc, count))

    return (outerBag, innerBags)

if __name__ == "__main__":
    bagDict = {}
    lines = getInput()
    for line in lines:
        outerBag, innerBags = parseBag(line)
        bagDict[outerBag] = innerBags
    print(len(getSuperBags([], [], 'shinygold', bagDict)))
    print(getRequiredBagsInBag('shinygold', bagDict) - 1)