import math

# Part 1
# https://math.stackexchange.com/questions/163080/
def spiral(n):
	k = math.ceil((math.sqrt(n)-1)/2)
	t = 2*k + 1
	m = t*t
	t = t-1

	if n >= (m-t):
		return Point(k-(m-n), -k)
	else:
		m = (m-t)

	if n >= (m-t):
		return Point(-k, -k+(m-n))
	else:
		m = m-t

	if n >= (m-t):
		return Point(-k+(m-n), k)
	else:
		return Point(k, k-(m-n-t))

def distance(start, end):
	return abs(end.X - start.X) + abs(end.Y - start.Y)

class Point(object):
	def __init__(self, x, y):
		self.X = x
		self.Y = y

	def __str__(self):
		return "Point(%s,%s)"%(self.X, self.Y) 

print distance(spiral(1), Point(0,0))
print distance(spiral(12), Point(0,0))
print distance(spiral(23), Point(0,0))
print distance(spiral(1024), Point(0,0))
print distance(spiral(325489), Point(0,0))

# Part 2
def sum_of_neighbors(grid, target):
	sum = 0
	sum += grid[target.X][target.Y+1]
	sum += grid[target.X+1][target.Y+1]
	sum += grid[target.X+1][target.Y]
	sum += grid[target.X+1][target.Y-1]
	sum += grid[target.X][target.Y-1]
	sum += grid[target.X-1][target.Y-1]
	sum += grid[target.X-1][target.Y]
	sum += grid[target.X-1][target.Y+1]
	return sum

def part_2 (grid, threshold):
	origin = Point(len(grid) / 2, len(grid) / 2)
	grid[origin.X][origin.Y] = 1
	for i in range (2, 10000):
		spiralPoint = spiral(i)
		target = withOrigin(origin, spiralPoint)
		value = sum_of_neighbors(grid, target)
		if value > threshold:
			return value
		grid[target.X][target.Y] = value
	return -1

def withOrigin(origin, target):
	return Point(int(origin.X + target.X), int(origin.Y + target.Y))

grid = [[0 for x in range(20)] for y in range(20)]

print part_2(grid, 325489)