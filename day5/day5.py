import re

input = "day5input.txt"
numTowers = 9


def part1():
    inputDone = False
    moveMatcher = "move (\d+) from (\d) to (\d)"
    towers = []

    for i in range(0, numTowers):
        towers.append([])

    with open(input) as f:
        for line in f.read().splitlines():
            # create starting configuration
            if not inputDone:
                inputDone = generateTowers(towers, line)

            # check to see if we have move instructions via REGEX and WALRUS OPERATOR!!!
            elif x := re.match(moveMatcher, line):
                numMoves = int(x.group(1))
                src = int(x.group(2))
                dest = int(x.group(3))

                # each box is moved one at a time so we have to pop each value off individually and add them to the
                # destination stack
                for i in range(0, numMoves):
                    value = towers[src - 1].pop()
                    towers[dest - 1].append(value)

        # print the final string
        finalStr = ""
        for tower in towers:
            finalStr += tower.pop()
        print(finalStr)


def part2():
    inputDone = False
    moveMatcher = "move (\d+) from (\d) to (\d)"
    towers = []

    for i in range(0, numTowers):
        towers.append([])

    with open(input) as f:
        for line in f.read().splitlines():
            # create starting configuration
            if not inputDone:
                inputDone = generateTowers(towers, line)

            # check to see if we have move instructions via REGEX and WALRUS OPERATOR!!!
            elif x := re.match(moveMatcher, line):
                numMoves = int(x.group(1))
                src = int(x.group(2))
                dest = int(x.group(3))

                # Since multiple crates can be moved one a time, we need to grab the list in order that is going to
                # be moved. This is done via subsets and extend. Extend allows us to combine 2 lists. Have to make sure
                # we update the src tower to remove the crates that were moved off. This is also done with subsets
                crates = towers[src - 1][len(towers[src - 1]) - numMoves:]
                towers[dest - 1].extend(crates)
                towers[src - 1] = towers[src - 1][:len(towers[src - 1]) - numMoves]

        finalStr = ""
        for tower in towers:
            finalStr += tower.pop()
        print(finalStr)


def generateTowers(towers, line):
    count = 0
    for c in line:
        # if we find a digit we are done with the input and can return true
        if c.isdigit():
            return True
        # if we find a number, we have to find out what stack it is in. A letter appears every 4th number so
        # we divide by 4 to find which stack it is in. and add the value to the FRONT of the stack. this means
        # the value to be popped off the stack is at the BACK of the stack
        if c.isalpha():
            index = max(0, int((count - 1) / 4))
            towers[index].insert(0, c)
        count += 1
    return False

part1()
part2()
