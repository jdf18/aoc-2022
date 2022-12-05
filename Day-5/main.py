class Stack:
	def __init__(self):
		self.crates = []
	def add_crate(self, crate):
		if crate == ' ': return
		self.crates.append(crate)

	def pop(self, number: int) -> list[str]:
		out = []
		# print(f'pop {number} - {self.crates}')
		for i in range(number):
			out.append(self.crates.pop())
		out.reverse()
		return out

	def push(self, crates: list[str]):
		crates.reverse()
		self.crates.extend(crates)

	def __repr__(self):
		return str(self.crates)

	def top(self):
		self.crates.reverse()
		for i in self.crates:
			if not i == ' ':
				self.crates.reverse()
				return i
		return ' '

class Stack2(Stack):
	def push(self, crates: list[str]):
		self.crates.extend(crates) 

class Instruction:
	def __init__(self, line: str):
		parts = line.split(' ')
		self.line = line
		self.no_boxes = int(parts[1])
		self.pick_stack = int(parts[3])-1
		self.drop_stack = int(parts[5])-1

	def __tuple__(self):
		return (
			self.no_boxes,
			self.pick_stack,
			self.drop_stack
		)
	def __repr__(self):
		return f"inst - {self.line}"

class Crane:
	def __init__(self, stacks: list[Stack]):
		self.stacks: list[Stack] = stacks
		self.instructions: list[Instruction] = []

	def load_instructions(self, instructions: list[Instruction]):
		self.instructions.extend(instructions)

	def execute(self):
		while len(self.instructions):
			inst = self.instructions.pop()
			#print(inst)
			crates = self.stacks[inst.pick_stack].pop(inst.no_boxes)
			self.stacks[inst.drop_stack].push(crates)
			#print(self)

	def __repr__(self):
		out = ''
		for i, s in enumerate(self.stacks):
			out += str(i+1) + s.__repr__() + '\n'
		return out

if __name__ == "__main__":
	with open("Day-5\instructions.dat") as file:
		lines = file.readlines()
	positions_index = lines.index("# positions\n")
	instructions_index = lines.index("# instructions\n")

	position_lines = lines[positions_index+1 : instructions_index]
	instruction_lines = list(map(str.strip, lines[instructions_index+1:]))
	instruction_lines.reverse()
	
	no_stacks = len(position_lines.pop().replace(' ',''))
	stacks = [Stack() for i in range(no_stacks-1)]
	position_lines.reverse()
	for line in position_lines:
		for i, j in enumerate(range(1, 4*no_stacks-6, 4)):
			stacks[i].add_crate(line[j])
	
	instructions = []
	for line in instruction_lines:
		instructions.append(Instruction(line))

	crane = Crane(stacks)
	crane.load_instructions(instructions)
	crane.execute()
	print('Part 1:',''.join(map(Stack.top, crane.stacks)))

	# part 2
	with open("Day-5\instructions.dat") as file:
		lines = file.readlines()
	positions_index = lines.index("# positions\n")
	instructions_index = lines.index("# instructions\n")

	position_lines = lines[positions_index+1 : instructions_index]
	instruction_lines = list(map(str.strip, lines[instructions_index+1:]))
	instruction_lines.reverse()
	
	no_stacks = len(position_lines.pop().replace(' ',''))
	stacks = [Stack2() for i in range(no_stacks-1)]
	position_lines.reverse()
	for line in position_lines:
		for i, j in enumerate(range(1, 4*no_stacks-6, 4)):
			stacks[i].add_crate(line[j])
	
	instructions = []
	for line in instruction_lines:
		instructions.append(Instruction(line))

	crane = Crane(stacks)
	crane.load_instructions(instructions)
	crane.execute()
	print('Part 2:',''.join(map(Stack.top, crane.stacks)))
