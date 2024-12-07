with open("2024\\day1\\input.txt", "r") as f:
    input = f.read()

leftlist = []
hashmap = {}

total = 0

lines = input.split("\n")
for line in lines:
    left, right = line.split("   ")
    left = int(left)
    right = int(right)
    leftlist.append(left)
    if hashmap.get(right) == None:
        hashmap[right] = 0
    hashmap[right] += 1


for l in leftlist:
    count = hashmap.get(l, 0)
    total += count * l

print (total)