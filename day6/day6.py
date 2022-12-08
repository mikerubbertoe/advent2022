input = "day6input.txt"

def getMarker(size):
    markerFound = False
    counter = 0

    with open(input) as f:
        for line in f.read().splitlines():
            while not markerFound:
                markerCheck = line[counter:counter + size]
                if len(set(markerCheck)) == size:
                    markerFound = True
                    print(counter + size)
                else:
                    counter += 1

getMarker(4)
getMarker(14)
