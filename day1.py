maxCalories1 = 0
maxCalories2 = 0
maxCalories3 = 0
currCalories = 0
inputFile = "day1input.txt"

with open(inputFile) as f:
    for line in f:
        if len(line) == 0 or line == "\n":
            if currCalories > maxCalories1:
                maxCalories3 = maxCalories2
                maxCalories2 = maxCalories1
                maxCalories1 = currCalories

            elif currCalories > maxCalories2:
                maxCalories3 = maxCalories2
                maxCalories2 = currCalories

            elif currCalories > maxCalories3:
                maxCalories3 = currCalories

            currCalories = 0
        else:
            currCalories += int(line)

print(maxCalories1 + maxCalories2 + maxCalories3)
