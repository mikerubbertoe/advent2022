import numpy as np
input = "day8input.txt"


def part1():
    visible = 0
    nparray = None
    with open(input) as f:
        trees =  f.read().splitlines()
        visible += (2 * len(trees)) + (2 * len(trees[0])) - 4
        nparray = np.empty((0,len(trees)), int)
        for row in range(0, len(trees)):
            tmp = []
            for col in range(0, len(trees[row])):
                tmp.append(int(trees[row][col]))

            nparray = np.append(nparray, [tmp], axis=0)


    for x in range(1, len(nparray) - 1):
        for y in range(1, len(nparray[x]) - 1):
            aboveMax = nparray[:x].max(axis=0)
            belowMax = nparray[x + 1:].max(axis=0)
            leftMax = nparray[x][:y].max(axis=0)
            rightMax = nparray[x][y + 1:].max(axis=0)
            if (nparray[x][y] > aboveMax[y]) or (nparray[x][y] > belowMax[y]) or (nparray[x][y] > leftMax) or (nparray[x][y] > rightMax):
                visible += 1
    print(visible)


def part2():
    visible = 0
    nparray = None
    with open(input) as f:
        trees =  f.read().splitlines()
        visible += (2 * len(trees)) + (2 * len(trees[0])) - 4
        nparray = np.empty((0,len(trees)), int)
        for row in range(0, len(trees)):
            tmp = []
            for col in range(0, len(trees[row])):
                tmp.append(int(trees[row][col]))

            nparray = np.append(nparray, [tmp], axis=0)

    score = 0

    for y in range(1, len(nparray) - 1):
        for x in range(1, len(nparray[y]) - 1):

            up = 0
            down = 0
            left = 0
            right = 0
            #find up
            arr = nparray[:y]
            for i in range(len(arr) - 1, -1, -1):
                up += 1
                if arr[i][x] >= nparray[y][x]:
                    break

            #find down
            arr = nparray[y+1:]
            for i in range(0, len(arr)):
                down += 1
                if arr[i][x] >= nparray[y][x]:
                    break

            # find left
            arr = nparray[y][:x]
            for i in range(len(arr) - 1, -1, -1):
                left += 1
                if arr[i] >= nparray[y][x]:
                    break

            # find right
            arr = nparray[y][x + 1:]
            for i in range(0, len(arr)):
                right += 1
                if arr[i] >= nparray[y][x]:
                    break

            if (up * down * left * right) > score:
                score = up * down * left * right

    print(score)
part1()
part2()