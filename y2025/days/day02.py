"""

"""
from re import fullmatch


def d2parse(data):
	line = data[0]
	result = []
	split_line = line.split(',')
	for elem in split_line:
		parts = elem.split('-')
		result.append(parts)

	return result

def d2p1(data):
	result = 0

	for elem in data:
		start = int(elem[0])
		end = int(elem[1]) + 1

		for i in range(start, end):
			converted_i = str(i)
			if len(converted_i) % 2 == 0:
				half = len(converted_i) // 2
				part1 = converted_i[:half]
				part2 = converted_i[half:]
				if part1 == part2:
					result += i

	return result


def d2p2(data):
	result = 0
	for elem in data:
		start = int(elem[0])
		end = int(elem[1]) + 1
		for i in range(start, end):
			converted_i = str(i)
			for regexp_len in range((len(converted_i) // 2) + 1):
				if fullmatch(fr'({converted_i[:regexp_len]})+', converted_i) is not None:
					result += i
					break
	return result
