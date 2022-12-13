import json


def loadFile():
    fileToOpen = input("0: example.txt 1: input.txt ")
    if fileToOpen == "0":
        return open("example.txt", "r", encoding="utf-8")
    if fileToOpen == "1":
        return open("input.txt", "r", encoding="utf-8")


def parseList(lis: str):
    lis = json.loads(lis)
    return lis


def packetPairHandler(packetPair):
    firstPacket = packetPair[0]
    secondPacket = packetPair[1]

    return compare(firstPacket, secondPacket)


def compare(firstPacket, secondPacket):
    #print(f"Compare {firstPacket} vs {secondPacket}")

    if isinstance(firstPacket, int) and isinstance(secondPacket, int):
        return intCompare(firstPacket, secondPacket)

    elif isinstance(firstPacket, list) and isinstance(secondPacket, int):
        return compare(firstPacket, [secondPacket])

    elif isinstance(firstPacket, int) and isinstance(secondPacket, list):
        return compare([firstPacket], secondPacket)

    elif isinstance(firstPacket, list) and isinstance(secondPacket, list):
        maxSize = max(len(firstPacket), len(secondPacket))
        for i in range(maxSize):
            first = firstPacket[i] if i < len(firstPacket) else None
            second = secondPacket[i] if i < len(secondPacket) else None

            if first is None:
                #print("Left side ran out of items, so inputs are in the right order")
                return True
            elif second is None:
                #print("Right side ran out of items, so inputs are in the wrong order")
                return False

            result = compare(firstPacket[i], secondPacket[i])
            if result is not None:
                return result


def intCompare(firstInt, secondInt):
    if firstInt < secondInt:
        #print("Left side is smaller, so inputs are in the right order")
        return True
    elif firstInt == secondInt:
        return None
    elif firstInt > secondInt:
        #print("Right side is smaller, so inputs are in the wrong order")
        return False


def part1():
    file = loadFile()

    # remove blank lines
    file = [line[:-1] for line in file if line != "\n"]

    # get packets
    packets = []
    for line in file:
        packets.append(parseList(line))

    # pair packets
    packetPairs = []
    for i in range(0, len(packets)-1, 2):
        packetPairs.append((packets[i], packets[i+1]))

    # handle packet pairs
    correctIndices = []
    for i, pair in enumerate(packetPairs):
        if packetPairHandler(pair):
            correctIndices.append(i+1)
            print()
            
    # compute sum
    print(f"Correct indices: {correctIndices}")
    sumOfCorrectIndices = sum(correctIndices)
    print(f"Sum of correct indices: {sumOfCorrectIndices}")
    return sumOfCorrectIndices

def sortingFunc(firstPacket, secondPacket):
    if packetPairHandler((firstPacket, secondPacket)):
        return -1
    else:
        return 1

def part2():
    file = loadFile()
    
    file = [line[:-1] for line in file if line != "\n"]
    
    packets = []
    for line in file:
        packets.append(parseList(line))
        
    # add divider packets
    packets.append([[2]])
    packets.append([[6]])
    
    # sort packets via bubble sort
    for i in range(len(packets)):
        for j in range(len(packets)-1):
            if sortingFunc(packets[j], packets[j+1]) == 1:
                packets[j], packets[j+1] = packets[j+1], packets[j]
    
    # get indices of divider packets
    dividerIndices = []
    for i, packet in enumerate(packets):
        if packet == [[2]] or packet == [[6]]:
            dividerIndices.append(i+1)
            
    # multiply indices
    product = 1
    for i in dividerIndices:
        product *= i
    
    print(product)

def main():
    #part1()
    part2()


if __name__ == "__main__":
    main()
