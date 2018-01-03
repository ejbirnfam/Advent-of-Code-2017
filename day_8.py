from collections import defaultdict
from operator import add, sub, lt, le, gt, ge, eq, ne

registers = defaultdict(int)
operatormap = {"<": lt, "<=": le, ">": gt, ">=": ge, "==": eq, "!=": ne}
maximum = 0

for line in open('day8.txt'):
    variable, operation, value, _, variable2, operation2, value2 = line.split()
    operation = sub if operation == "dec" else add
    operation2 = operatormap[operation2]

    if operation2(registers[variable2], int(value2)):
        registers[variable] = operation(registers[variable], int(value))

    maximum = registers[variable] if registers[variable] > maximum else maximum

print(max(registers.values()))
print maximum