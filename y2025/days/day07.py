"""

"""
def d7parse(data):
	"""

	"""
	result = []
	for line in data:
		result.append(list(line))

	return result


def d7p1(data):
	"""
	modifies data to draw all the tachyon pathes while calculating split
	"""
	result = 0
	for y in range(1, len(data)):
		for x in range(len(data[y])):
			if data[y-1][x] == 'S':
				data[y][x] = '|'

			if data[y-1][x] == '|':
				if data[y][x] == '^':
					result += 1
					data[y][x-1] = '|'
					data[y][x+1] = '|'
				else:
					data[y][x] = '|'

	return result


def d7p2_old(data):
	"""
	brute force, doesn't work in acceptable amount of time on actual puzzle
	"""
	result = 0

	lasers = []
	for x in range(len(data[0])):
		if data[0][x] == 'S':
			lasers.append([1, x])
			result += 1
			break

	while lasers:
		y, x = lasers.pop()
		try:
			if data[y+1][x] == '^':
				result += 1
				lasers.append([y+1, x-1])
				lasers.append([y+1, x+1])
			else:
				lasers.append([y+1, x])
		except IndexError:
			pass

	return result


def explore_path(data, start, saved_results):
	"""
	recursive explore with memoization
	"""
	if start in saved_results:
		return saved_results[start]

	y, x = start
	subresult = 0
	if y != len(data) - 1:
		if data[y+1][x] == '^':
			subresult += 1
			subresult += explore_path(data, (y+1, x-1), saved_results)
			subresult += explore_path(data, (y+1, x+1), saved_results)
		else:
			subresult += explore_path(data, (y+1, x), saved_results)

	saved_results[(y, x)] = subresult
	return subresult


def d7p2(data):
	"""

	"""
	result = 0
	saved_results = {}

	startx = 0
	for x in range(len(data[0])):
		if data[0][x] == 'S':
			startx = x
			result += 1
			break

	result += explore_path(data, (1, startx), saved_results)
	return result
