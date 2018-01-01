# Part 1
def string_input(string):
    return [n.replace("(", "").replace(")", "").replace(",", "") for n in string.split() if n != "->"]

with open('day7_practice.txt') as fileinput:
    data = [string_input(line) for line in fileinput.read().strip().splitlines()]

flat_list = [item for sublist in data for item in sublist if not item.isdigit()]
answer = [x for x in flat_list if flat_list.count(x) == 1]
print answer

# Part 2
def find_children_weights(name):
    children_weights = []
    for child in children[name]:
        children_weights.append(calculate_weight(child))
    return children_weights

def check_balance(name):
    if children[name] == []:
        return True
    children_weights = find_children_weights(name)
    return len(set(children_weights)) == 1

def unbalanced_child(name):
    child_weights = find_children_weights(name)
    for child in children[name]:
        curr_weight = calculate_weight(child)
        if child_weights.count(curr_weight) == 1:
            return child

def calculate_weight(name):
    total = values[name]
    for child in children[name]:
        total += calculate_weight(child)
    return total

children = {}
values = {}
for line in open('day7_practice.txt'):
    name = list(line.replace(',','').strip().split())
    values[name[0]] = int(name[1].replace('(','').replace(')',''))
    children[name[0]] = name[3:]

start = 'tknk'

while not check_balance(start):
    parent = start
    start = unbalanced_child(start)

child = children[parent][0]
if child == start:
    child = children[parent][1]
print values[start] - calculate_weight(start) + calculate_weight(child)

