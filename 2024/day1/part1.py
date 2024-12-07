with open("2024\\day1\\input.txt", "r") as f:
    input = f.read()

leftlist = []
rightlist = []

total = 0

lines = input.split("\n")
for line in lines:
    left, right = line.split("   ")
    left = int(left)
    right = int(right)
    leftlist.append(left)
    rightlist.append(right)

leftlist.sort()
rightlist.sort()

for l, r in zip(leftlist, rightlist):
    total += abs(l-r)

print(total)




