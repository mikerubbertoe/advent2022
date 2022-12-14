import numpy as np
input = "day14input.txt"

def makeCave():
    x = [0] * 600
    y = [0] * 600
    arr = np.array([x] * 300)
    with open(input) as f:
        for line in f.read().splitlines():
            splitLine = line.split(' -> ')
            lastX, lastY = -1, -1
            for coordinate in splitLine:
                coord = coordinate.split(',')
                currX, currY = int(coord[0]), int(coord[1])

                if currX != lastX and currY != lastY:
                    arr[currY][currX] = -1
                elif currX != lastX:
                    for i in range(min(currX, lastX), max(currX, lastX) + 1):
                        arr[currY][i] = -1
                elif currY != lastY:
                    for i in range(min(currY, lastY), max(currY, lastY) + 1):
                        arr[i][currX] = -1
                lastX = currX
                lastY = currY
    return arr

def part1():
    arr = makeCave()
    sand = 0
    while True:
        notStuck = True
        sandX = 500
        sandY = 0
        while notStuck:
            if sandY + 1 == len(arr):
                print(sand)
                return sand

            if arr[sandY + 1][sandX] == 0:
                sandY += 1
            elif arr[sandY + 1][sandX - 1] == 0:
                sandY += 1
                sandX -= 1
            elif arr[sandY + 1][sandX + 1] == 0:
                sandY += 1
                sandX += 1
            else:
                notStuck = False
                sand += 1
                arr[sandY][sandX] = 1


part1()
