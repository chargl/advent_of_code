"""

"""
def mult(lst: list[int]):
	"""
	multiplies all elements from a list together
	"""
	result = 1
	for i in lst:
		result *= i
	return result


def d6parse(data):
	"""
	{
		1: {
			"numbers": ["  1", "321", ...]
			'function": sum/mult
		}, ...
	}
	Updated for part 2
	"""
	problems = {}
	func_pos = []
	for i in range(len(data[-1])):
		if data[-1][i] == '+' or data[-1][i] == '*':
			func_pos.append(i)

	for line in data[:-1]:
		last = 0
		for i in range(len(func_pos) - 1):
			if i not in problems:
				problems[i] = {'numbers': []}
			problems[i]['numbers'].append(line[func_pos[i]:func_pos[i + 1]-1])
			last = i + 1

		if last not in problems:
			problems[last] = {'numbers': []}
		problems[last]['numbers'].append(line[func_pos[last]:])


	split_line = data[-1].split()
	for i in range(len(split_line)):
		if split_line[i] == '*':
			problems[i]['function'] = mult
		elif split_line[i] == '+':
			problems[i]['function'] = sum
	return problems


def d6p1(data):
	"""

	"""
	result = 0
	for _, problem in data.items():
		func = problem['function']
		numbers = [int(i) for i in problem['numbers']]
		result += func(numbers)
	return result


def d6p2(data):
	"""

	"""
	result = 0
	for _, problem in data.items():
		func = problem['function']
		nb_numbers = len(problem['numbers'][0])
		actual_numbers = ['' for _ in range(nb_numbers)]
		for number in problem['numbers']:
			for i in range(nb_numbers):
				actual_numbers[i] += number[i]

		result += func([int(i) for i in actual_numbers])
	return result
