"""
aoc y2025 day 1
https://adventofcode.com/2025/day/1
"""

def d1parse(data):
	"""
	parse
	"""
	return data

def d1p1(data):
	"""

	"""
	result = 0
	current = 50
	for line in data:
		change = int(line[1:])
		move = change % 100
		if line.startswith('R'):
			current += move
			if current > 99:
				current -= 100
		else:
			current -= move
			if current < 0:
				current += 100

		if current == 0:
			result += 1

	return result

def d1p2(data):
	"""

	"""
	result = 0
	current = 50
	for line in data:
		direction = line[0]
		change = int(line[1:])
		rotations = 0

		if direction == 'R':
			total_move = current + change
			rotations = total_move // 100
			current = total_move % 100

		else:
			flipped_current = (100 - current) % 100
			rotations = (flipped_current + change) // 100
			current = (current - change) % 100

		result += rotations

	return result
