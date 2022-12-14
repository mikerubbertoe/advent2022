import heapq as heap

class Node:
    def __init__(self, height, location, top):
        self.height = height
        self.cost = 1
        self.location = location
        self.top = top

    def __repr__(self):
        return "{0}".format(self.location)


def dijstra(graph, startingNode):
    pq = []
    not_visited = set()
    distance = [float('inf')] * (len(graph) * len(graph[0]))
    distance[startingNode] = 0
    for i in range(len(graph) * len(graph[0])):
        not_visited.add(i)

    heap.heappush(pq, (0, startingNode))

    while pq:
        currNode = heap.heappop(pq)
        #print(currNode)
        not_visited.remove(currNode[1])
        for n in get_neighbors(currNode[1], len(graph), len(graph[0])):
            y = int(n / len(graph[0]))
            x = int(n % len(graph[0]))
            nextNode = graph[y][x]
            thisNode = graph[int(currNode[1] / len(graph[0]))][int(currNode[1] % len(graph[0]))]
            cost = graph[y][x].cost

            if thisNode.height + 1 < nextNode.height:
                continue

            if n in not_visited:
                old_cost = distance[n]
                new_cost = distance[thisNode.location] + cost

                if new_cost < old_cost:
                    distance[len(graph[0])*y+x] = new_cost
                    heap.heappush(pq,(new_cost,graph[y][x].location))

    for i in graph:
        for j in i:
            if j.top:
                return distance[j.location]


def get_neighbors(node, a, b):
    neighbors = []
    currY = int(node / b)
    currX = int(node % b)
    for x,y in [[0,1],[-1,0],[1,0],[0,-1]]:
        newX = x + currX
        newY = y + currY
        if 0<=newX<b and 0<=newY<a:
            neighbors.append(int((newY * b) + newX))
    return neighbors

def parse_input(filename):
    i = []
    counter = 0
    low = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            x = []

            for char in line:
                value = 0
                top = False
                if char == 'E':
                    value = ord('z') - 96
                    top = True
                elif char == 'S':
                    value = 0
                else:
                    value = ord(char) - 96
                x.append(Node(value, counter, top))
                if char == 'a':
                    low.append(counter)
                counter += 1
            i.append(x)
    return i, low

def part1():
    input, _ = parse_input('day12input.txt')
    dijstra(input, 1620)


def part2():
    input, low = parse_input('day12input.txt')
    lowest = float('inf')
    for start in low:
        if (ret := dijstra(input, start)) < lowest:
            lowest = ret
    print(lowest)

part2()
