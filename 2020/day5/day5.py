with open("day5\\input.txt", "r") as f:
    input = f.read()

boardingpasses = input.split("\n")

max_rows = 128
max_cols = 8

rows = []
cols = []
seatIDs = []

for boardingpass in boardingpasses:
    bp_rows = boardingpass[:7]
    bp_cols = boardingpass[-3:]

    F=0
    B=128
    M_row=(F+B)//2

    for r in bp_rows:
        if r == "F": 
            B=M_row
            M_row=(F+B)//2


        if r == "B":
            F=M_row
            M_row=(F+B)//2

    rows.append(M_row)    

    L=0
    R=8
    M_col=(L+R)//2

    for c in bp_cols:
        if c == "L":
            R=M_col
            M_col=(L+R)//2

        if c == "R":
            L=M_col
            M_col=(L+R)//2
        
    cols.append(M_col)

    ID = (M_row*8)+M_col

    seatIDs.append(ID)
    

highestID = 0

for n in seatIDs:
    if (n > highestID):
        highestID = n

#print(highestID)
    

# part two

sortedIDs = sorted(seatIDs)

for entry in sortedIDs:
    if ((entry+1) not in sortedIDs and (entry+2) in sortedIDs):
        print(entry+1)

