import math

fileToLoad = input("0: example.txt, 1: input.txt")


if fileToLoad == "0":
    file = open("example.txt", "r")
elif fileToLoad == "1":
    file = open("input.txt", "r")


def getMonkeyDefinitions(content: str):
    content = content.split("\n\n")
    return content


class Monkey:
    def __init__(self, definition: str):
        definition = definition.split("\n")

        # monkey number
        self.num = int(definition[0].split(" ")[1][0])

        # items
        self.items = []
        for item in definition[1].split(" ")[4:]:
            item = item.replace(",", "")
            self.items.append(int(item))

        # operation
        op = definition[2].split(" ")[6:]
        if op[0] == "*" and op[1] != "old":
            self.operation = lambda x: x * int(op[1])
        elif op[0] == "+" and op[1] != "old":
            self.operation = lambda x: x + int(op[1])
        elif op[0] == "*" and op[1] == "old":
            self.operation = lambda x: x * x
        elif op[0] == "+" and op[1] == "old":
            self.operation = lambda x: x + x

        # test
        self.divisbleBy = definition[3].split(" ")[-1]
        self.trueMonkey = int(definition[4].split(" ")[-1])
        self.falseMonkey = int(definition[5].split(" ")[-1])
        self.test = lambda x: x % int(self.divisbleBy) == 0

        # inspection counter
        self.count = 0

    def __str__(self):
        return f"Monkey {self.num} has items {self.items} and operation {self.operation} and test {self.test}"

    def addToItems(self, item: int):
        self.items.append(item)

    def execute(self):
        for item in self.items:
            item = self.operation(item)

            # divide by 3 and round down to nearest integer
            # item = item // 3

            # new worry calc
            item = item % 9699690

            # test the item
            if self.test(item):
                # self.items.remove(rawItem)
                addToMonkey(self.trueMonkey, item)
            else:
                # self.items.remove(rawItem)
                addToMonkey(self.falseMonkey, item)

            self.count += 1

        self.items = []


def makeAllMonkeys(file: str) -> list:
    monkeys = []

    for definition in getMonkeyDefinitions(file.read()):
        monkeys.append(Monkey(definition))

    return monkeys


monkeys = makeAllMonkeys(file)


def addToMonkey(num: int, item: int):
    global monkeys
    monkeys[num].addToItems(item)


def runRounds(rounds: int, monkeys: list):
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.execute()


def calcMonkeyBusses(monkeys: list):
    # get top two monkeys with highest count
    topMonkeys = sorted(
        monkeys, key=lambda monkey: monkey.count, reverse=True)[:2]
    print(topMonkeys[0].count * topMonkeys[1].count)


def part1():
    global monkeys
    runRounds(20, monkeys)
    calcMonkeyBusses(monkeys)

# part1()


def getDivisibleBy(monkeys):
    nums = []
    for monkey in monkeys:
        nums.append(int(monkey.divisbleBy))
    return nums


def getWorryFactor(monkeys):
    nums = getDivisibleBy(monkeys)
    print(math.lcm(*nums))


def part2():
    global monkeys
    runRounds(10000, monkeys)
    calcMonkeyBusses(monkeys)


getWorryFactor(monkeys)
part2()
