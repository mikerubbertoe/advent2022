from anytree import Node

input = "day7input.txt"
total = 0
removal = [300000000000000000000000000, '&']

# generate the directory tree and store the sizes and file type of everything
def generateTree():
    root = Node("&")
    count = 0
    currNode = root
    with open(input) as f:
        for line in f.read().splitlines():
            splitLine = line.split(' ')

            # if we find a command
            if splitLine[0] == '$':
                # only care about change in dir so we only capture the cd command
                if splitLine[1] == "cd":
                    # move back up the tree to maintain the structure properly
                    if splitLine[2] == "..":
                        currNode = currNode.parent
                    else:
                        # otherwise, move down the directory path based on what value was specified in the input
                        for child in currNode.children:
                            if child.name == splitLine[2]:
                                currNode = child
                                break

            # if we find a file, create a node for the file and store the size and type and count all the space
            # used so we can use it in part 2
            elif splitLine[0].isdigit():
                Node(splitLine[1], parent=currNode, type="file", size=int(splitLine[0]))
                count += int(splitLine[0])
            # if we find a directory create a node for the dir and store the type
            else:
                Node(splitLine[1], parent=currNode, type="dir")
    return root, count

# recursively go through the tree a 2nd time to see what directories are smaller than 1000000 for part 1 as
# well as keep track of the smallest file that can be removed for the update. Node will be the current done
# the traversal is on and minSpace is a constant size value for the min size of the directory that can be
# removed for the update. Yes I know global variables bad but I dont care.
def countSize(node, minSpace):
    global total
    global removal
    size = 0
    # for each child
    for child in node.children:
        # count the size
        if child.type == "file":
            size += child.size
        # if its a directory then add the count of all the files in that sub directory
        else:
            size += countSize(child, minSpace)

    # check for part 1 if the total size is less than 100000
    if size <= 100000:
        total += size
    # check for part 2 if the smallest file for removal is actually the smallest
    if minSpace <= size < removal[0]:
        removal[0] = size
        removal[1] = node.name

    # return the size of the directory
    return size


def part1():
    root, _ = generateTree()
    countSize(root, 300000000000000000000000000)
    print(total)


def part2():
    root, totalSpace = generateTree()
    minSpace = 30000000 - (70000000 - totalSpace)
    countSize(root, minSpace)
    print(removal)


part1()
part2()
