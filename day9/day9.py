input = "day9input.txt"

def part1():
    head_x, head_y, tail_x, tail_y = 0, 0, 0, 0
    visited = {(0, 0)}
    x_move = 1
    y_move = 1

    with open(input) as f:
        for line in f.read().splitlines():
            direction = line.split(' ')[0]
            movement  = line.split(' ')[1]

            for i in range(0, int(movement)):
                match direction:
                    case "R":
                        head_x += 1
                        x_move = 1
                    case "L":
                        head_x -= 1
                        x_move = -1
                    case "U":
                        head_y += 1
                        y_move = 1
                    case "D":
                        head_y -= 1
                        y_move = -1

                if abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1:
                    if head_x != tail_x:
                        tail_x += x_move
                    if head_y != tail_y:
                        tail_y += y_move

                visited.add((tail_x, tail_y))

    print(len(visited))

def part2():
    head_x, head_y, last_x, last_y = 0, 0, 0, 0
    knots = {
        0: (0, 0),
        1: (0, 0),
        2: (0, 0),
        3: (0, 0),
        4: (0, 0),
        5: (0, 0),
        6: (0, 0),
        7: (0, 0),
        8: (0, 0),
        9: (0, 0)
    }
    visited = {(0, 0)}

    with open(input) as f:
        for line in f.read().splitlines():
            direction = line.split(' ')[0]
            movement = line.split(' ')[1]

            for i in range(0, int(movement)):
                match direction:
                    case "R":
                        head_x += 1
                    case "L":
                        head_x -= 1
                    case "U":
                        head_y += 1
                    case "D":
                        head_y -= 1

                knots[0] = (head_x, head_y)
                for x in range(1, len(knots)):
                    curr_x = knots[x][0]
                    curr_y = knots[x][1]
                    last_x = knots[x - 1][0]
                    last_y = knots[x - 1][1]
                    x_diff = last_x - curr_x
                    y_diff = last_y - curr_y
                    if abs(x_diff) > 1 or abs(y_diff) > 1:
                        if knots[x - 1][0] != knots[x][0]:
                            curr_x = curr_x + 1 if x_diff > 0 else curr_x - 1
                        if knots[x - 1][1] != knots[x][1]:
                            curr_y = curr_y + 1 if y_diff > 0 else curr_y - 1

                    knots[x] = (curr_x, curr_y)

                visited.add(knots[9])
    print(len(visited))


part1()
part2()
