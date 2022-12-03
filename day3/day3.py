input = "day3input.txt"

with open(input) as f:
    intersection = {}
    sum = 0
    for line in f:
        set1 = set()
        half = int(len(line) / 2)
        for i in range(0, half):
            set1.add(line[i])

        for i in range(half + 1, len(line)):
            if line[i] in set1:
                value = (ord(line[i]) - 96) if ord(line[i]) > 96 else (ord(line[i]) - 38)
                if line[i] not in intersection:
                    intersection[line[i]] = value
                else:
                    intersection[line[i]]  += value

                sum += value
                break
    print(sum)
