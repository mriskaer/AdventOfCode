with open("day3\\input.txt", "r") as f:
    input = f.read()

lines = input.split("\n")
lines = [l for l in lines if len(l) > 0]

tree = "#"
nRows = len(lines)
nCols = len(lines[0])

slopeStrategies = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


stratTrees = []

for right, down in slopeStrategies:
    col = 0
    row = 0
    nTrees = 0
    while row < nRows:
        colIdx = col % nCols

        if lines[row][colIdx] == tree:
            nTrees += 1

        col += right
        row += down

    stratTrees.append(nTrees)

total = stratTrees[0]
for i in range(1, len(stratTrees)):
    total = total *  stratTrees[i]

print(total)