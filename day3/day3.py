input = "day3input.txt"


def part1():
    with open(input) as f:
        intersection = {}
        sum = 0
        for line in f:
            set1 = set()
            half = int(len(line) / 2)
            for i in range(0, half):
                set1.add(line[i])

            for i in range(half, len(line)):
                if line[i] in set1:
                    value = (ord(line[i]) - 96) if ord(line[i]) > 96 else (ord(line[i]) - 38)
                    if line[i] not in intersection:
                        intersection[line[i]] = value
                    else:
                        intersection[line[i]]  += value

                    sum += value
                    break
        print(sum)


def part2():
    with open(input) as f:
        count = 0
        sets = []
        sum = 0

        for line in f:
            if count == 3:
                result = sets[0].intersection(sets[1], sets[2])
                char = next(iter(result))
                value = (ord(char) - 96) if ord(char) > 96 else (ord(char) - 38)
                sum += value
                count = 0
                sets = []

            set1 = set()
            for i in line.strip():
                set1.add(i)
            sets.append(set1)
            count += 1
    print(sum)

part2()