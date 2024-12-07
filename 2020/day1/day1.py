with open("day1\\input.txt", "r") as f:
    input = f.read()

lines = [int(d) for d in input.split("\n") if len(d) > 0]
nLines = len(lines)

#part 1
for i in range(0, nLines):
    for j in range(i, nLines):
        if lines[i] + lines[j] == 2020:
            print(lines[i] * lines[j])

#part 2
for i in range(0, nLines):
    for j in range(i, nLines):
        for k in range(j, nLines):
            if lines[i] + lines[j] + lines[k] == 2020:
                print(lines[i] * lines[j] * lines[k])