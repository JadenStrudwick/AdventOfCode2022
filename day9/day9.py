class HeadKnotTail:
    knots = []
    tailposhistory = [(0, 0)]
    
    def __init__(self, knotsize):
        for i in range(knotsize):
            self.knots.append((0,0))
    
    def getX(self, knotnum):
        return self.knots[knotnum][0]
    
    def getY(self, knotnum):
        return self.knots[knotnum][1]
    
    def setX(self, knotnum, x):
        self.knots[knotnum] = (x, self.getY(knotnum))
        
    def setY(self, knotnum, y):
        self.knots[knotnum] = (self.getX(knotnum), y)
        
    def increaseX(self, knotnum, num):
        self.setX(knotnum, self.getX(knotnum) + num)
        
    def increaseY(self, knotnum, num):
        self.setY(knotnum, self.getY(knotnum) + num)
            
    def moveHead(self, direction, num):
        if direction == 'R':
            for _ in range(num):
                self.increaseX(0, 1)
                self.moveKnot(1)
        elif direction == 'L':
            for _ in range(num):
                self.increaseX(0, -1)
                self.moveKnot(1)
        elif direction == 'U':
            for _ in range(num):
                self.increaseY(0, 1)
                self.moveKnot(1)
        elif direction == 'D':
            for _ in range(num):
                self.increaseY(0, -1)
                self.moveKnot(1)
            
    def isAdjacent(self, knotnum):
        tailx = self.getX(knotnum)
        taily = self.getY(knotnum)
        headx = self.getX(knotnum-1)
        heady = self.getY(knotnum-1)
        
        if (headx-1, heady-1) == (tailx, taily):
            return True
        elif (headx, heady-1) == (tailx, taily):
            return True
        elif (headx+1, heady-1) == (tailx, taily):
            return True
        elif (headx-1, heady) == (tailx, taily):
            return True
        elif (headx+1, heady) == (tailx, taily):
            return True
        elif (headx-1, heady+1) == (tailx, taily):
            return True
        elif (headx, heady+1) == (tailx, taily):
            return True
        elif (headx+1, heady+1) == (tailx, taily):
            return True
        elif (headx, heady) == (tailx, taily):
            return True
        else:
            return False
        
    def moveKnot(self, knotnum):
        tailx = self.getX(knotnum)
        taily = self.getY(knotnum)
        headx = self.getX(knotnum-1)
        heady = self.getY(knotnum-1)
            
        while not self.isAdjacent(knotnum):
            # print(f"Knot {knotnum} is not adjacent to Knot {knotnum-1}")
            # if head and tail are on the same x axis
            # move tail 1 step towards head
            if headx == tailx:
                if heady > taily:
                    self.increaseY(knotnum, 1)
                elif heady < taily:
                    self.increaseY(knotnum, -1)

            # if head and tail are on the same y axis
            # move tail 1 step towards head
            elif heady == taily:
                if headx > tailx:
                    self.increaseX(knotnum, 1)
                elif headx < tailx:
                    self.increaseX(knotnum, -1)

            # if head and tail are not on the same axis
            # move tail 1 step towards head on both axis
            else:
                if headx > tailx:
                    self.increaseX(knotnum, 1)
                elif headx < tailx:
                    self.increaseX(knotnum, -1)
                if heady > taily:
                    self.increaseY(knotnum, 1)
                elif heady < taily:
                    self.increaseY(knotnum, -1)

            self.logOrRecur(knotnum)
                
    def logTailPos(self):
        tail = self.knots[-1]
        self.tailposhistory.append(tail)
        #print(tail)
        
    def logOrRecur(self, knotnum):
        if knotnum == len(self.knots) - 1:
            self.logTailPos()
        else:
            self.moveKnot(knotnum + 1)
            
def part2():
    file =  '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''
    contents = file.splitlines()
    
    file = open('input.txt', 'r')
    contents = file.read().splitlines()
    num_lines = sum(1 for line in contents)
    
    ht = HeadKnotTail(10)
    
    for i, line in enumerate(contents):
        print(f"Progress: {i+1}/{num_lines}")
        (direction, num) = line.split(' ')
        ht.moveHead(direction, int(num))
        
    locationset = set(ht.tailposhistory)
    print(len(locationset))
    
part2()
    
