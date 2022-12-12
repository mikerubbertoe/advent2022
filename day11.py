import re

input = "day11input.txt"

class Monkey:
    def __init__(self, name, items, operation, test, trueTest, falseTest):
        self.name = name
        self.items = [int(item) for item in items]
        self.modItems = [int(item) for item in items]
        self.operation = operation.strip()
        self.test = int(test)
        self.trueTest = int(trueTest)
        self.falseTest = int(falseTest)
        self.itemsInspected = 0

    def __str__(self):
        return("{0} {1}".format(self.name, self.items))

    def calculateWorryLevel(self, item):
        splitOp = self.operation.split(' ')
        operator = splitOp[1]
        value = int(splitOp[2]) if splitOp[2].isdigit() else item

        newValue = 0
        match operator:
            case '+':
                newValue = item + value
            case '-':
                newValue = item - value
            case '*':
                newValue = item * value
            case '/':
                newValue = item / value

        return int(newValue)

    def throwingLocation(self, item):
        return self.trueTest if item % self.test == 0 else self.falseTest

def part1():
    monkeys = []
    with open(input) as f:
        while True:
            mon = f.readline().strip()
            if not mon:
                break

            startingItems = f.readline().strip().split(' ', 2)[2].split((', '))
            operation = f.readline().strip().split('=', 1)[1]
            test = f.readline().strip().split(' ')[-1]
            trueTest = f.readline().strip().split(' ')[-1]
            falseTest = f.readline().strip().split(' ')[-1]
            f.readline()

            newMonkey = Monkey(mon, startingItems, operation, test, trueTest, falseTest)
            monkeys.append(newMonkey)
        print(monkeys)

    for i in range(0, 20):
        for x in range(0, len(monkeys)):
            for item in monkeys[x].items:
                newItem = int(monkeys[x].calculateWorryLevel(item) / 3)
                location = monkeys[x].throwingLocation(newItem)

                monkeys[x].itemsInspected += 1
                monkeys[location].items.append(newItem)

            monkeys[x].items = []
    for monkey in monkeys:
        print(monkey.itemsInspected)

def part2():
    monkeys = []
    with open(input) as f:
        while True:
            mon = f.readline().strip()
            if not mon:
                break

            startingItems = f.readline().strip().split(' ', 2)[2].split((', '))
            operation = f.readline().strip().split('=', 1)[1]
            test = f.readline().strip().split(' ')[-1]
            trueTest = f.readline().strip().split(' ')[-1]
            falseTest = f.readline().strip().split(' ')[-1]
            f.readline()

            newMonkey = Monkey(mon, startingItems, operation, test, trueTest, falseTest)
            monkeys.append(newMonkey)
        print(monkeys)

    for i in range(0, 100):
        for x in range(0, len(monkeys)):
            for item in monkeys[x].items:
                newItem = int(monkeys[x].calculateWorryLevel(item))
                location = monkeys[x].throwingLocation(newItem)

                monkeys[x].itemsInspected += 1
                monkeys[location].items.append(newItem)
                #monkeys[location].modItems.append(newItem % monkeys[x].test)
            monkeys[x].items = []
            #monkeys[x].modItems = []
        print("{0} {1} {2} {3}".format(monkeys[0].items, monkeys[1].items, monkeys[2].items, monkeys[3].items))
        #print("{0} {1} {2} {3}".format(monkeys[0].modItems, monkeys[1].modItems, monkeys[2].modItems, monkeys[3].modItems))

    for monkey in monkeys:
        print(monkey.itemsInspected)

#part1()
part2()
