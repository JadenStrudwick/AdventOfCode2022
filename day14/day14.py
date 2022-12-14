
def loadFile():
    fileToLoad = input("0: example.txt | 1: input.txt ")
    if fileToLoad == "0":
        file = open("example.txt", "r", encoding="utf-8")
    elif fileToLoad == "1":
        file = open("input.txt", "r", encoding="utf-8")
    return file

class World:
    grid = [[]]
    paths = []
    
    minWidth = float("inf")
    maxWidth = float("-inf")
    
    minHeight = 0
    maxHeight = float("-inf")
    
    sands = []
    
    def __init__(self, file):
        for line in file:
            self.convertLineToPath(line)
        self.findMinMax()
        self.makeGrid()
        self.addPaths()
    
    
    def convertLineToPath(self, line):
        line = line.replace("->", "")
        line = line.replace("\n", "")
        line = line.split("  ")
        
        path = []
        for coord in line:
            x, y = coord.split(",")
            path.append((int(x), int(y)))
        
        self.paths.append(path)
        
    def findMinMax(self):
        for path in self.paths:
            for coord in path:
                x, y = coord
                if x < self.minWidth:
                    self.minWidth = x
                if x > self.maxWidth:
                    self.maxWidth = x
                if y < self.minHeight:
                    self.minHeight = y
                if y > self.maxHeight:
                    self.maxHeight = y
    
    def makeGrid(self):
        self.grid = [['.' for x in range(self.minWidth, self.maxWidth + 1)] for y in range(self.minHeight, self.maxHeight + 1)]
        
    def addPaths(self):
        for path in self.paths:
            for i in range(0, len(path) - 1):
                x1, y1 = path[i]
                x2, y2 = path[i + 1]
                                
                x1 -= self.minWidth
                y1 -= self.minHeight
                
                x2 -= self.minWidth
                y2 -= self.minHeight
                                
                if x1 == x2:
                    if y1 > y2:
                        for y in range(y2, y1 + 1):
                            self.grid[y][x1] = "#"
                    else:
                        for y in range(y1, y2 + 1):
                            self.grid[y][x1] = "#"
                elif y1 == y2:
                    if x1 > x2:
                        for x in range(x2, x1 + 1):
                            self.grid[y1][x] = "#"
                    else:
                        for x in range(x1, x2 + 1):
                            self.grid[y1][x] = "#"
                                 
                
    def printGrid(self):
        for i, row in enumerate(self.grid):
            print(i, end=" ")
            for char in row:
                print(char, end="")
            print()
                    
    def addSand(self):
        sandx = 500 - self.minWidth
        sandy = 0 - self.minHeight
                
        sandFall = True
        
        while sandFall:
            if self.canFallDown(sandx, sandy):
                sandy += 1
            elif self.canFallLeft(sandx, sandy):
                sandx -= 1
                sandy += 1
            elif self.canFallRight(sandx, sandy):
                sandx += 1
                sandy += 1
            else:
                sandFall = False
                self.grid[sandy][sandx] = "o"
                self.sands.append((sandx, sandy))
                    
    def canFallDown(self, sandx, sandy):
        if self.grid[sandy + 1][sandx] == "#" or self.grid[sandy + 1][sandx] == "o":
            return False
        else:
            return True
        
    def canFallLeft(self, sandx, sandy):
        if self.grid[sandy + 1][sandx - 1] == "#" or self.grid[sandy + 1][sandx - 1] == "o":
            return False
        else:
            return True
        
    def canFallRight(self, sandx, sandy):
        if self.grid[sandy + 1][sandx + 1] == "#" or self.grid[sandy + 1][sandx + 1] == "o":
            return False
        else:
            return True
        

def part1():
    file = loadFile()
    world = World(file)
    
    world.printGrid()
    
    sandCount = 0
    try:
        while True:
            world.addSand()
            sandCount += 1
    except IndexError:
        pass

    world.printGrid()
    print(sandCount)
    
class World2:
    grid = [[]]
    paths = []
    
    minWidth = float("inf")
    maxWidth = float("-inf")
    
    minHeight = 0
    maxHeight = float("-inf")
    
    sands = []
    
    def __init__(self, file):
        for line in file:
            self.convertLineToPath(line)
        self.findMinMax()
        self.makeGrid()
        self.addPaths()
    
    
    def convertLineToPath(self, line):
        line = line.replace("->", "")
        line = line.replace("\n", "")
        line = line.split("  ")
        
        path = []
        for coord in line:
            x, y = coord.split(",")
            path.append((int(x), int(y)))
        
        self.paths.append(path)
        
    def findMinMax(self):
        for path in self.paths:
            for coord in path:
                x, y = coord
                if x < self.minWidth:
                    self.minWidth = x - 100000
                if x > self.maxWidth:
                    self.maxWidth = x + 100000
                if y < self.minHeight:
                    self.minHeight = y
                if y > self.maxHeight:
                    self.maxHeight = y
    
    def makeGrid(self):
        self.grid = [['.' for x in range(self.minWidth, self.maxWidth + 1)] for y in range(self.minHeight, self.maxHeight + 1)]
        
        # blank row 
        self.grid.append(['.' for x in range(self.minWidth, self.maxWidth + 1)])
        
        # filled row
        self.grid.append(['#' for x in range(self.minWidth, self.maxWidth + 1)])
        
    def addPaths(self):
        for path in self.paths:
            for i in range(0, len(path) - 1):
                x1, y1 = path[i]
                x2, y2 = path[i + 1]
                                
                x1 -= self.minWidth
                y1 -= self.minHeight
                
                x2 -= self.minWidth
                y2 -= self.minHeight
                                
                if x1 == x2:
                    if y1 > y2:
                        for y in range(y2, y1 + 1):
                            self.grid[y][x1] = "#"
                    else:
                        for y in range(y1, y2 + 1):
                            self.grid[y][x1] = "#"
                elif y1 == y2:
                    if x1 > x2:
                        for x in range(x2, x1 + 1):
                            self.grid[y1][x] = "#"
                    else:
                        for x in range(x1, x2 + 1):
                            self.grid[y1][x] = "#"
                                 
                
    def printGrid(self):
        for i, row in enumerate(self.grid):
            print(i, end="\t")
            for char in row:
                print(char, end="")
            print()
                    
    def addSand(self):
        sandx = 500 - self.minWidth
        sandy = 0 - self.minHeight
                
        sandFall = True
        
        while sandFall:
            if self.canFallDown(sandx, sandy):
                sandy += 1
            elif self.canFallLeft(sandx, sandy):
                sandx -= 1
                sandy += 1
            elif self.canFallRight(sandx, sandy):
                sandx += 1
                sandy += 1
            else:
                sandFall = False
                self.grid[sandy][sandx] = "o"
                self.sands.append((sandx, sandy))
                    
    def canFallDown(self, sandx, sandy):
        if self.grid[sandy + 1][sandx] == "#" or self.grid[sandy + 1][sandx] == "o":
            return False
        else:
            return True
        
    def canFallLeft(self, sandx, sandy):
        if self.grid[sandy + 1][sandx - 1] == "#" or self.grid[sandy + 1][sandx - 1] == "o":
            return False
        else:
            return True
        
    def canFallRight(self, sandx, sandy):
        if self.grid[sandy + 1][sandx + 1] == "#" or self.grid[sandy + 1][sandx + 1] == "o":
            return False
        else:
            return True
    
def isSourceCovered(world):
    if len(world.sands) == 0:
        return False
    
    lastSand = world.sands[-1]
    
    x = lastSand[0] + world.minWidth
    y = lastSand[1] + world.minHeight
    
    print(lastSand)
    if (x,y) == (500, 0):
        return True
    else:
        return False
    
def part2():
    file = loadFile()
    world2 = World2(file)
    #world2.printGrid()
    
    sandCount = 0
    while not isSourceCovered(world2):
        world2.addSand()
        sandCount += 1
    
    #world2.printGrid()
    print(sandCount)
    
    
def main():
    #part1()
    part2()

if __name__ == "__main__":
    main()
    