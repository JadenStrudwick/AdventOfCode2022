from dijkstar import Graph, find_path

def loadFile():
    fileToOpen = input("0: example.txt, 1: input.txt ")
    if fileToOpen == "0":
        file = open("example.txt", "r")
    elif fileToOpen == "1":
        file = open("input.txt", "r")
    return file.read()

def convertToGrid(content: str):
    content = content.split("\n")
    grid = []
    vertexCount = 0
    sourceVertex = 0
    destinationVertex = 0
    for line in content:
        row = []
        for char in line:
            if char == "S":
                sourceVertex = vertexCount
            elif char == "E":
                destinationVertex = vertexCount
            row.append(charToHeight(char))
            vertexCount += 1
        grid.append(row)
    return grid, sourceVertex, destinationVertex

def charToHeight(char: str):
    if char == "S":
        return charToHeight("a")
    elif char == "E":
        return charToHeight("z")
    return ord(char) - 97

def convertToGraph(grid):
    graph = Graph()
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            currentVertexValue = grid[i][j]
            currentVertexNumber = getVertexNumber(grid, i, j)
            
            if i != 0:
                # calculate up cost
                upVertexValue = grid[i-1][j]
                upVertexNumber = getVertexNumber(grid, i-1, j)
                cost = upVertexValue - currentVertexValue
                if cost <= 1:
                    graph.add_edge(currentVertexNumber, upVertexNumber, 1)
            if i != len(grid) - 1:
                # calculate down cost
                downVertexValue = grid[i+1][j]
                downVertexNumber = getVertexNumber(grid, i+1, j)
                cost = downVertexValue - currentVertexValue
                if cost <= 1:
                    graph.add_edge(currentVertexNumber, downVertexNumber, 1)
            if j != 0:
                # calculate left cost
                leftVertexValue = grid[i][j-1]
                leftVertexNumber = getVertexNumber(grid, i, j-1)
                cost = leftVertexValue - currentVertexValue
                if cost <= 1:
                    graph.add_edge(currentVertexNumber, leftVertexNumber, 1)
            if j != len(row) - 1:
                # calculate right cost
                rightVertexValue = grid[i][j+1]
                rightVertexNumber = getVertexNumber(grid, i, j+1)
                cost = rightVertexValue - currentVertexValue
                if cost <= 1:
                    graph.add_edge(currentVertexNumber, rightVertexNumber, 1)
    return graph
        
def getVertexNumber(grid, x, y):
    return x * len(grid[0]) + y

def part1():
    file = loadFile()
    grid, src, dest = convertToGrid(file)
    graph = convertToGraph(grid)
    print(find_path(graph, src, dest)[-1])
    
def getAllLowestVerticeNumbers(grid):
    lowestVerticeNumbers = []
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            if grid[i][j] == 0:
                lowestVerticeNumbers.append(getVertexNumber(grid, i, j))
    return lowestVerticeNumbers
    
def part2():
    file = loadFile()
    grid, src, dest = convertToGrid(file)
    lowestVerticeNumbers = getAllLowestVerticeNumbers(grid)
    graph = convertToGraph(grid)
    
    pathcosts = []
    for num in lowestVerticeNumbers:
        try:
            print(num, find_path(graph, num, dest)[-1])
            pathcosts.append(find_path(graph, num, dest)[-1])
        except:
            continue
    
    print(min(pathcosts))
    
def main():
    #part1()
    part2()
    
if __name__ == "__main__":
    main()