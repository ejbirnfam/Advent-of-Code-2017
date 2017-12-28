
# Day 2
import itertools

# Part 1
def digits(string):
    return [int(n) for n in string.split()]

with open('day2.txt') as fileinput:
    data = [digits(line) for line in fileinput.read().strip().splitlines()]

data_len = len(data)
data_sum = 0

for i in range (data_len):
	data_sum += max(data[i]) - min(data[i])

print data_sum

# Part 2
def digits(string):
    return [int(n) for n in string.split()]

with open('day2.txt') as fileinput:
    data = [digits(line) for line in fileinput.read().strip().splitlines()]

data_len = len(data)
data_sum = 0

for i in range (data_len):
	row_len = len(data[i])
	for j in range (row_len):
		k = j + 1
		while k < row_len:
			if (data[i][j] % data[i][k]) == 0:
				data_sum += data[i][j] / data[i][k]
			elif (data[i][k] % data[i][j]) == 0:
				data_sum += data[i][k] / data[i][j]
			k = k + 1

print data_sum