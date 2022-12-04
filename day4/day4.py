import re
input = "day4input.txt"

# 2low >= 1low and 2high <= 1high
# 1low >= 2low and 1high <= 2high
def part1():
    dup = 0
    with open(input) as f:
        for line in f.read().splitlines():
            workers = line.split(',')
            worker1_low, worker1_high = workers[0].split('-')
            worker2_low, worker2_high = workers[1].split('-')

            if (int(worker1_low) >= int(worker2_low) and int(worker1_high) <= int(worker2_high)) or \
            (int(worker2_low) >= int(worker1_low) and int(worker2_high) <= int(worker1_high)):
                dup += 1

    print(dup)


def part2():
    regex = '([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)'
    overlap = 0
    with open(input) as f:
        for line in f.read().splitlines():
            result = re.search(regex, line)
            worker1_low, worker1_high = int(result.group(1)), int(result.group(2))
            worker2_low, worker2_high = int(result.group(3)), int(result.group(4))

            #only 2 cases that will ensure that there is no overlap. Easier to check for those than to check
            #for all the cases that do have overlap
            if not(worker2_low > worker1_high or worker1_low > worker2_high):
                overlap += 1
    print(overlap)


part1()
part2()