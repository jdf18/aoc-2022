class Rucksack:
	def __init__(self, items) -> None:
		self.first, self.second = items[:len(items)//2], items[len(items)//2:]
		for l in self.first:
			for k in self.second:
				if l == k:
					self.common = l
					return
		print('Its all gone wrong')
		
	def get_value(self):
		def value(letter: str) -> int:
			if letter.isupper():
				return ord(letter) - ord('A') + 27
			return ord(letter) - ord('a') + 1

		return value(self.common)

class Group:
	def __init__(self, rucksacks):
		for i in rucksacks[0]:
			for j in rucksacks[1]:
				for k in rucksacks[2]:
					if i == j == k:
						self.common = i
						return
	def get_value(self):
		def value(letter: str) -> int:
			if letter.isupper():
				return ord(letter) - ord('A') + 27
			return ord(letter) - ord('a') + 1

		return value(self.common)
					

if __name__ == '__main__':
	with open('Day-3/rucksacks.dat') as file:
		lines = file.readlines()
	sacks = map(Rucksack, lines)
	total = sum(map(Rucksack.get_value, sacks))
	print('Part 1:', total)

	with open('Day-3/rucksacks.dat') as file:
		lines = file.readlines()
	groups = []
	for i in range(len(lines)//3):
		groups.append(Group((lines.pop(),lines.pop(),lines.pop())))
	total = sum(map(Group.get_value, groups))
	print('Part 2:', total)

	
		