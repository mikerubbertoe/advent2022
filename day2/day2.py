
#
# r = 1
# p = 2
# s = 3
#
# r r = 0 (tie)
# r p = -1(win) (2+6)
# r s = -2(loss) (3+0)
#
# p r = 1 (loss) (1+0)
# p p = 0 (tie) (2+3)
# p s = -1 (win) (3+6)
#
# s r = 2 (win) (1+6)
# s p = 1 (loss) (2+0)
# s s = 0 (tie) (3+3)
#
# if 0 = tie
# if +odd = loss
# if -odd = win
# if +even = win
# if -even = loss
#
# if difference is 0: tie
# if difference is -1: win

def part1():
    input = "day2input.txt"
    score = 0
    board = {
        'A' : 1,
        'B' : 2,
        'C' : 3,
        'X' : 1,
        'Y' : 2,
        'Z' : 3
    }

    with open(input) as f:
        for line in f:
            choices = line.strip().split(' ')
            c1 = board[choices[0]]
            c2 = board[choices[1]]
            diff = c1 - c2
            score += c2

            if diff > 0:
                if diff % 2 == 0:
                    score += 6
            elif diff < 0:
                if diff % 2 != 0:
                    score += 6
            else:
                score += 3
    print(score)




def part2():
    input = "day2input.txt"
    score = 0
    board = {
        'A' : 1,
        'B' : 2,
        'C' : 3
    }

    with open(input) as f:
        for line in f:
            choices = line.strip().split(' ')
            c1 = board[choices[0]]
            c2 = choices[1]
            if c2 == 'X':
                score = score + 3 if c1 == 1 else score + (c1 - 1) % 3
            elif c2 == 'Y':
                score += 3 + c1
            elif c2 == 'Z':
                score = score + 6 + 3 if c1 == 2 else score + 6 + ((c1 + 1) % 3)

    print(score)

# A X = 3 + 0 = 3
# A Y = 1 + 3 = 4
# A Z = 2 + 6 = 8
# B X = 1 + 0 = 1
# B Y = 2 + 3 = 5
# B Z = 3 + 6 + 9
# C X = 2 + 0 + 2
# C Y = 3 + 3 + 6
# C Z = 1 + 6 + 7 --> 45

part1()
part2()