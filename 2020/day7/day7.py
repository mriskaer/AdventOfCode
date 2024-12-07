with open("day7\\input.txt", "r") as f:
    input = f.read()

rules = input.split("\n")

sgb = "shiny gold"
num_of_bags = 0

adjacency_list = {}

for rule in rules:
    current_bag, contains = rule.split(" contain ")

    current_bag = current_bag.replace(" bags", "")

    if (current_bag not in adjacency_list):
        adjacency_list[current_bag] = []

    contains = contains.split(", ")

    for innerbag in contains:
        innerbag = innerbag.replace(".", "")
        innerbag = innerbag.replace(" bags", "")
        innerbag = innerbag.replace(" bag", "")
        amount, innerbag = innerbag.split(" ", 1)

        if (innerbag == "other"):
            continue

        adjacency_list[current_bag].append(innerbag)
        
        #print(innerbag)

def has_shiny (bag):
    children = adjacency_list[bag]
    if sgb in children:
        return True
    
    for child in children:
        if has_shiny(child):
            return True

    return False

for bag in adjacency_list:
    if has_shiny(bag):
        num_of_bags += 1


print(num_of_bags)