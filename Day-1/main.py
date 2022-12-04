class Elf:
	def __init__(self):
		self.calories = 0
	def add_calories(self, cal):
		self.calories += cal
	def __repr__(self) -> str:
		return str(self.calories)

def parse_file(filename):
	elves = []
	with open(filename) as file:
		current_elf = Elf()
		for line in file.readlines():
			if line == '\n':
				elves.append(current_elf)
				current_elf = Elf()
			else:
				current_elf.add_calories(int('0'+line.strip()))
	return elves


if __name__ == "__main__":
	elves = parse_file('Day-1\calories.dat')
	print(elves)
	sort = sorted(elves, key=lambda x:x.calories, reverse=True)
	print('Part 1:', sort[0].calories)
	print('Part 2:', sort[0].calories+sort[1].calories+sort[2].calories)