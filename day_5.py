# Day 5

# Part 1
# with open("day5.txt") as f:
#     content = f.readlines()
# content = [int(x.strip()) for x in content]

# content_length = len(content)

# steps = 0
# i = 0

# while i < content_length and i >= 0:
# 	old_i = i
# 	i += content[old_i]
# 	content[old_i] += 1
# 	steps += 1

# print steps

# Part 2
with open("day5.txt") as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

content_length = len(content)

steps = 0
i = 0

while i < content_length and i >= 0:
	old_i = i
	i += content[old_i]
	if content[old_i] >= 3:
		content[old_i] -= 1
	else:
		content[old_i] += 1
	steps += 1

print steps