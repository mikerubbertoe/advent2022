import heapq as heap
import time

class Node:
    def __init__(self, height, location):
        self.height = height
        self.cost = 1
        self.location = location

    def __str__(self):
        return self.height


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
            y = int(n / len(graph))
            x = int(n % len(graph[0]))
            nextNode = graph[y][x]
            cost = graph[y][x].cost

            if currNode[1].height + 1 < graph[y][x].height:
                continue

            if n in not_visited:
                old_cost = distance[n]
                new_cost = distance[currNode[1].location] + cost

                if new_cost < old_cost:
                    distance[len(graph[0])*y+x] = new_cost
                    heap.heappush(pq,(new_cost,graph[y][x]))

    print(distance[-1])
    print(len(distance))

def get_neighbors(node, a, b):
    neighbors = []
    currY = int(node / a)
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
    with open(filename) as f:
        for line in f:
            line = line.strip()
            x = []
            for char in line:
                value = ord(char) - 96 if ord(char) - 96 > 0 else 0
                x.append(Node(value, counter))
                counter += 1
            i.append(x)
    return i

input = parse_input('day12input.txt')

dijstra(input, 0)
