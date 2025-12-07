"""

"""
def d5parse(data):
	"""

	"""
	ranges = []
	ingredients = []

	for line in data:
		splt = line.split('-')
		if len(splt) > 1:
			start = int(splt[0])
			end = int(splt[1])
			ranges.append([start, end])
		else:
			try:
				ingredient = int(line)
			except ValueError:
				pass
			else:
				ingredients.append(ingredient)
	return [ranges, ingredients]


def d5p1(data):
	"""

	"""
	ranges, ingredients = data
	result = 0
	for ingredient in ingredients:
		for range in ranges:
			start, end = range
			if ingredient >= start and ingredient <= end:
				result += 1
				break
	return result


def d5p2(data):
	"""

	"""
	result = 0
	ranges, _ = data
	ranges.sort()

	updated_ranges = []

	for i in range(len(ranges)):
		start, end = ranges[i]
		add = True
		for r in updated_ranges:
			s, e = r

			if start > e:
				continue

			elif end < s:
				continue

			elif s <= start and end <= e:
				add = False
				break

			elif start <= s and s <= end and end <= e:
				end = s - 1

			elif s <= start and start <= e and e < end:
				start = e + 1

		if add:
			updated_ranges.append([start, end])

	for r in updated_ranges:
		start, end = r
		result += end-start + 1

	return result
