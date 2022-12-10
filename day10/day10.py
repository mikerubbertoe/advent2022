input = "day10input.txt"

def part1():
    cycle = 0
    count = 1
    total = 0
    last  = [0]

    with open(input) as f:
        for line in f.read().splitlines():
            instructiton = line.split(' ')


            if cycle == 20 or (cycle - 20) % 40 == 0:
                total += cycle * count
                print(total, cycle * count)

            if len(instructiton) == 2:
                cycle += 1
                if cycle == 20 or (cycle - 20) % 40 == 0:
                    total += cycle * count
                    print(total, cycle * count)
                cycle += 1
                count += int(instructiton[1])
            else:
                cycle += 1

    print(total)

part1()