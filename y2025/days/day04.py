"""


"""
def d4parse(data):
	"""

	"""
	result = []
	for line in data:
		result.append(list(line))
	return result

def adjacent_pos(data, y, x):
	adjacent = []
	for line in range(y-1, y+2):
			for col in range(x-1, x+2):
				if line != y or col != x:
					if line >= 0 and line < len(data) and col >= 0 and col < len(data[0]):
						adjacent.append([line, col])

	return adjacent

def d4p1(data):
	"""

	"""
	result = 0
	for y in range(len(data)):
		for x in range(len(data[y])):
			if data[y][x] == '@':
				adjacent = 0
				for pos in adjacent_pos(data, y, x):
					y1, x1 = pos
					if data[y1][x1] == '@':
						adjacent += 1


				if adjacent < 4:
					result += 1
	return result



def d4p2(data):
	"""

	"""
	result = 0
	cont = True
	while cont:
		cont = False
		remove = []
		for y in range(len(data)):
			for x in range(len(data[y])):
				if data[y][x] == '@':
					adjacent = 0
					for pos in adjacent_pos(data, y, x):
						y1, x1 = pos
						if data[y1][x1] == '@':
							adjacent += 1

					if adjacent < 4:
						remove.append([y, x])
						cont = True
		result = result + len(remove)
		for elem in remove:
			y, x = elem
			data[y][x] = 'x'
	return result
