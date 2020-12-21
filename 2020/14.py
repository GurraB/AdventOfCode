import re

mem = {}
mask = 0
overwriteMask = 0
memoryMask = ''

def getInput():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            return lines

def parseMask(rawMask):
    global mask, overwriteMask
    mask = int(rawMask.replace('X', '1'), 2)
    overwriteMask = int(rawMask.replace('X', '0'), 2)

def applyMask(number):
    return ((number & mask) | overwriteMask)

def executeLineVersion1(line):
    global mask, mem
    if 'mask' in line:
        parseMask(line.split()[-1])
    else:
        numbers = re.findall(r'\d+', line)
        memoryAddress = int(numbers[0])
        value = int(numbers[1])
        mem[memoryAddress] = applyMask(value)

def decoderVersion1(lines):
    for line in lines:
        executeLineVersion1(line)
    
    res = 0
    for key in mem.keys():
        res += mem[key]
    print(res)

def parseFloatingAddress(address: str):
    if not 'X' in address:
        return [int(address, 2)]
    a0 = parseFloatingAddress(address.replace('X', '0', 1))
    a1 = parseFloatingAddress(address.replace('X', '1', 1))
    a0.extend(a1)
    return a0

def getAllAddresses(memoryAddress):
    global memoryMask
    memoryAddress = list(str(bin(int(memoryAddress)))[2:])[::-1]
    for i in range(len(memoryMask)):
        if i >= len(memoryAddress):
            memoryAddress.append('0')
        if memoryMask[i] == '0':
            continue
        else:
            memoryAddress[i] = memoryMask[i]
    return parseFloatingAddress(''.join(memoryAddress[::-1]))

def saveToMemVersion2(memoryAddress, value):
    for address in getAllAddresses(memoryAddress):
        mem[address] = value

def executeLineVersion2(line):
    global memoryMask, mem
    if 'mask' in line:
        memoryMask = list(line.split()[-1])[::-1]
    else:
        numbers = re.findall(r'\d+', line)
        memoryAddress = numbers[0]
        value = int(numbers[1])
        saveToMemVersion2(memoryAddress, value)

def decoderVersion2(lines):
    for line in lines:
        executeLineVersion2(line)
    res = 0
    for key in mem.keys():
        res += mem[key]
    print(res)

if __name__ == "__main__":
    lines = getInput()
    decoderVersion1(lines)
    mem = {}
    decoderVersion2(lines)