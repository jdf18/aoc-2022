class ElfPair:
	def __init__(self, line_in: str):
		self.line = line_in
		elf1, elf2 = map(str.strip, line_in.split(','))
		self.elf1_lower, self.elf1_higher = map(int, map(str.strip, elf1.split('-')))
		self.elf2_lower, self.elf2_higher = map(int, map(str.strip, elf2.split('-')))
	def get_contained(self):
		elf1_range = (self.elf1_higher - self.elf1_lower)
		elf2_range = (self.elf2_higher - self.elf2_lower)
		
		if elf1_range > elf2_range:
			if self.elf1_lower <= self.elf2_lower and self.elf2_higher <= self.elf1_higher:
				return True
		else:
			if self.elf2_lower <= self.elf1_lower and self.elf1_higher <= self.elf2_higher:
				return True
		return False

	def get_overlap(self):
		return max(self.elf1_lower, self.elf2_lower) <= min(self.elf1_higher, self.elf2_higher)


if __name__ == "__main__":
	with open('Day-4/cleaning.dat') as file:
		lines = file.readlines()
	pairs = map(ElfPair, lines)
	print('Part 1:',sum(map(ElfPair.get_contained, pairs)))
	pairs = map(ElfPair, lines)
	print('Part 2:',sum(map(ElfPair.get_overlap, pairs)))