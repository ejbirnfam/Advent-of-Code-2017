import itertools

# Part 1
def check_for_duplicates(input_list):
	return len(input_list) == len(set(input_list))

def words(string):
	return [n for n in string.split()]

with open('day4.txt') as fileinput:
	data = [words(line) for line in fileinput.read().strip().splitlines()]

data_length = len(data)
data_sum = 0

for i in range(data_length):
	if check_for_duplicates(data[i]):
		data_sum += 1

print data_sum

print check_for_duplicates(["aa", "bb", "cc", "dd", "ee"])
print check_for_duplicates(["aa", "bb", "cc", "dd", "aa"])
print check_for_duplicates(["aa", "bb", "cc", "dd", "aaa"])

# Part 2
def check_for_duplicates(input_list):
	data_length = len(input_list)
	for i in range(data_length):
		j = i + 1
		while j < data_length:
			if sorted(input_list[i]) == sorted(input_list[j]):
				return True
			j += 1
	return False

def words(string):
	return [n for n in string.split()]

with open('day4.txt') as fileinput:
	data = [words(line) for line in fileinput.read().strip().splitlines()]

data_sum = 0
data_length = len(data)

for i in range(data_length):
	if not check_for_duplicates(data[i]):
		data_sum += 1

print data_sum