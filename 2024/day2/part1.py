with open("2024\\day2\\input.txt", "r") as f:
    input = f.read() 
lines = input.split("\n")

lines = [line.split(" ") for line in lines]

count = 0

# for line in lines:
#     numberLine = [int(numString) for numString in line]
#     print(line, numberLine)

#     isBad=False

#     if sorted(numberLine) == numberLine or sorted(numberLine,reverse=True) == numberLine:
#         for i in range(len(numberLine)-1): 
#             dif = abs(numberLine[i] - numberLine[i+1])
#             if not (dif <= 3 and dif >= 1): 
#                 isBad = True
#                 break

#     else: 
#         isBad = True

#     if not isBad: 
#         count +=1    


for line in lines:
    numberLine = [int(numString) for numString in line]

    if not (sorted(numberLine) == numberLine or sorted(numberLine,reverse=True) == numberLine):
        continue

    isBad = False
    for i in range(len(numberLine)-1): 
        dif = abs(numberLine[i] - numberLine[i+1])
        if not (dif <= 3 and dif >= 1): 
            isBad = True
            break
    if isBad:
        continue

    count += 1    




print(count)
        

