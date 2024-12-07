with open("day6\\chrisinput.txt", "r") as f:
    input = f.read()

groups = input.split("\n\n") # split i grupper

count = 0

for group in groups: # for hver gruppe
    persons = group.split("\n") # split på linjer for hver person, der former en gruppe
    
    answers = [] # her skal hvert bogstav tilføjes, første gang det optræder, så jeg til sidst kan tælle læ

    hashmap = {}

    #print(persons)

    for person in persons:
        for char in person:
            if (char in hashmap.keys()):
                hashmap[char]+=1
            else:
                hashmap[char]=1
    
    for value in hashmap.values():
        if (value == len(persons)):
            count +=1


print(count)