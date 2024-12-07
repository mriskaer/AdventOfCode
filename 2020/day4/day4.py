with open("day4\\input.txt", "r") as f:
    input = f.read()

passports = input.split("\n\n")

reqKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

pps = 0

def checkNumber(n, minN, maxN):
    if not len(n) == 4:
        return False
    
    nN = int(n)
    if not (nN >= minN and nN <= maxN):
        return False

    return True

def check_byr(byr):
    return checkNumber(byr, 1920, 2002)

def check_iyr(iyr):
    return checkNumber(iyr, 2010, 2020)

def check_eyr(eyr):
    return checkNumber(eyr, 2020, 2030)

def check_hgt(height):
    if not len(height) > 3:
        return False

    numberPart = height[:len(height) - 2]
    lastTwo = height[-2:]

    if not (lastTwo == "cm" or lastTwo == "in"):
        return False

    try:
        number = int(numberPart)
    except:
        return False

    if lastTwo == "cm":
        if not (number >= 150 and number <= 193):
            return False

    else:
        if not (number >= 59 and number <= 76):
            return False
    
    return True

def check_hcl(hcl):
    ok_char = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    if not (len(hcl)==7):
        return False
    
    if not (hcl[0]=="#"):
        return False
    
    for c in hcl[1:]:
        if c not in ok_char:
            return False
    return True

def check_ecl(ecl):
    ok_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if not ecl in ok_ecl:
        return False
    return True

def check_pid(pid):
    if not len(pid) == 9:
        return False
    
    try: 
        int(pid)
    
    except:
        return False

    return True

keyDict = {
    "byr": check_byr,
    "iyr": check_iyr,
    "eyr": check_eyr,
    "hgt": check_hgt,
    "hcl": check_hcl,
    "ecl": check_ecl,
    "pid": check_pid
}

for passport in passports:
    passport = passport.replace("\n", " ")
    properties = passport.split(" ")

    propDict = {}
    for prop in properties:
        k, v = prop.split(":")
        
        if k == "cid":
            continue
        propDict[k] = v


    if not len(propDict) == len(reqKeys):
        continue
    #print(propDict)

    valid = True
    for key, value in propDict.items():
        if not keyDict[key](value):
            valid = False

    
    if valid:
        pps += 1

    

print(pps)

