import ast

input = "day13input.txt"

def check_packet(p1, p2):
    retval = 0

    for i in range(min(len(p1), len(p2))):

        #if they are both ints
        if type(p1[i]) == int and type(p2[i]) == int:
            if p1[i] < p2[i]:
                return 1
            elif p1[i] > p2[i]:
                return -1

        #if they are both lists
        elif type(p1[i]) == list and type(p2[i]) == list:
            retval = check_packet(p1[i], p2[i])
        #if one is a list and one is an int
        elif type(p1[i]) == list and type(p2[i]) == int:
            retval = check_packet(p1[i], [p2[i]])
        elif type(p1[i]) == int and type(p2[i]) == list:
            retval = check_packet([p1[i]], p2[i])
        if retval > 0:
            return 1
        if retval < 0:
            return -1

    if len(p1) < len(p2):
        return 1
    if len(p1) > len(p2):
        return - 1
    return 0

def part1():
    counter = 1
    total = 0
    with open(input) as f:
        while True:
            p1 = f.readline().strip()
            if not p1:
                print(total)
                return
            p1 = ast.literal_eval(p1)
            p2 = ast.literal_eval(f.readline().strip())
            retval = check_packet(p1, p2)
            if retval > 0:
                total += counter
            counter += 1
            f.readline()

def part2():
    sorted = [[[2]], [[6]]]
    with open(input) as f:
        for line in f.read().splitlines():
            inserted = False
            if not line:
                continue
            p1 = ast.literal_eval(line)
            for i in range(len(sorted)):
                if retval := check_packet(p1, sorted[i]) > 0:
                    sorted.insert(i, p1)
                    inserted = True
                    break
            if not inserted:
                sorted.append(p1)

    print(sorted.index([[2]]) + 1)
    print(sorted.index([[6]]) + 1)

part1()
part2()
