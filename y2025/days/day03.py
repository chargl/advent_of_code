

def d3parse(data):
	return data

def d3p1(data):
	result = 0
	for line in data:
		max = 0
		for i in range(len(line)):
			char1 = line[i]
			for char2 in line[i+1:]:
				current = int(f'{char1}{char2}')
				if current > max:
					max = current
		result += max
	return result

def d3p2(data):
	result = 0
	for line in data:
		batteries = []
		line_len = len(line)

		for i, c in enumerate(line):
			current = int(c)
			remaining = line_len - i - 1
			while batteries and current > batteries[-1] and len(batteries) + remaining >= 12:
				batteries.pop(-1)
			if len(batteries) < 12:
				batteries.append(current)

		line_result = int(''.join(str(n) for n in batteries))
		result += line_result
	return result
