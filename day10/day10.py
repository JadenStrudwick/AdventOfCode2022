# load input
file = open("input.txt", "r")

def instruction_parser(instruction: str, x, cycles):
    instruction = instruction.split(" ")
    if instruction[0] == "addx":
        return addx(int(instruction[1]), x, cycles)
    elif instruction[0] == "noop\n":
        return noop(x, cycles)

def addx(value, x, cycles):
    cycles.append((x * len(cycles), x))
    cycles.append((x * len(cycles), x))
    x += value    
    return x, cycles

def noop(x, cycles):
    cycles.append((x * len(cycles), x))    
    return x, cycles

def part1():
    x = 1
    cycles = [1]
    for instruction in file:
        x, cycles = instruction_parser(instruction, x, cycles)
    
    # for i, cycle in enumerate(cycles):
    #     print(f"{i}: {cycle}")
        
    total = 0

    # sum of 20th, 60th, 100th, 140th, 180th and 220th cycle
    for i in [20, 60, 100, 140, 180, 220]:
        print(f"{i}: {cycles[i]}")
        total += cycles[i][0]

    print(f"Total: {total}")

# part1()

class CRT:
    display = [['.' for _ in range(40)] for _ in range(6)]
    sprite = [0, 1, 2]
    
    def printDisplay(self):
        for row in self.display:
            print("".join(row))
        print("")
            
    def turnOn(self, x, y):
        self.display[y][x] = '#'
        
    def moveSprite(self, num):
        currentPos = self.sprite[1]
        newPos = currentPos + num
        self.sprite = [newPos - 1, newPos, newPos + 1]
    
    def printToDisplay(self, cyclenum):
        pixelNum = cyclenum - 1
        # find the column and row to print to
        columnToPrint = pixelNum % 40
        rowToPrint = pixelNum // 40
        
        # check if the sprite is in the way
        if columnToPrint in self.sprite:
            self.turnOn(columnToPrint, rowToPrint)
            
        # print the display
        self.printDisplay()
                    
                    
def instruction_parser2(instruction: str, x, cycles, crt):
    instruction = instruction.split(" ")
    if instruction[0] == "addx":
        return addx2(int(instruction[1]), x, cycles, crt)
    elif instruction[0] == "noop\n":
        return noop2(x, cycles, crt)
    
def addx2(value, x, cycles, crt):
    cycles.append((x * len(cycles), x))
    crt.printToDisplay(len(cycles))
    cycles.append((x * len(cycles), x))
    crt.printToDisplay(len(cycles))
    x += value    
    crt.moveSprite(value)
    return x, cycles
    
def noop2(x, cycles, crt):
    cycles.append((x * len(cycles), x))
    crt.printToDisplay(len(cycles))
    return x, cycles

def part2():
    x = 1
    cycles = []
    crt = CRT()
    
    for instruction in file:
        x, cycles = instruction_parser2(instruction, x, cycles, crt)
    
    crt.printDisplay()
    
part2()