# input = [0,2,7,0]
input = [10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]
final_outputs = [[]]
count_of_loops = 0

while input not in final_outputs:
	count_of_loops += 1
	final_outputs.append(input[:])
	input_length = len(input)
	max_value = max(input)
	max_index = input.index(max_value)
	input[max_index] = 0
	next_index = max_index + 1
	while max_value > 0:
		input[(next_index % input_length)] += 1
		max_value -= 1
		next_index += 1

print count_of_loops
repeat_index = [x for x in final_outputs].index(input)
print len(final_outputs) - repeat_index