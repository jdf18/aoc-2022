class Move:
	def __init__(self, opponent:str, play:str):
		self.opponent = (1 if opponent == 'A' else (2 if opponent == 'B' else 3))
		self.play = (1 if play == 'X' else (2 if play == 'Y' else 3))
	def __repr__(self) -> str:
		def conv(value) -> str:
			match value:
				case 1: return "rock"
				case 2: return "paper"
				case 3: return "scissors"
				case _: return str(value)
		return conv(self.opponent) + " -> " + conv(self.play)
	
	@staticmethod
	def calc_outcome(opp, play):
		match opp:
			case 1: # rock
				match play:
					case 1: return 3
					case 2: return 6
					case _: return 0
			case 2: # paper
				match play:
					case 1: return 0
					case 2: return 3
					case _: return 6
			case _: # scissors
				match play:
					case 1: return 6
					case 2: return 0
					case _: return 3

	def score(self) -> int:
		outcome = self.calc_outcome(self.opponent, self.play)
		return self.play + outcome

class Move2:
	def __init__(self, opponent: str, outcome: str):
		self.opponent = (1 if opponent == 'A' else (2 if opponent == 'B' else 3))
		self.outcome = (0 if outcome == 'X' else (3 if outcome == "Y" else 6))
		self.play = None
	
	def __repr__(self) -> str:
		if not self.play:
			self.play = self.get_play()
		def conv(value) -> str:
			match value:
				case 1: return "rock"
				case 2: return "paper"
				case 3: return "scissors"
				case _: return str(value)
		return conv(self.opponent) + " -> " + conv(self.play)

	def get_play(self):
		match self.opponent:
			case 1: # rock
				match self.outcome:
					case 0: return 3 # loss
					case 3: return 1
					case _: return 2
			case 2: # paper
				match self.outcome:
					case 0: return 1 # loss
					case 3: return 2
					case _: return 3
			case _:
				match self.outcome: # scissors
					case 0: return 2 # loss
					case 3: return 3
					case _: return 1

	def score(self) -> int:
		self.play = self.get_play()
		return self.play + self.outcome


def parse_file(filename, cls):
	moves = []
	with open(filename) as file:
		for line in file.readlines():
			moves.append(
				cls(*line.strip().split())
			)
	return moves


if __name__ == "__main__":
	moves = parse_file('Day-2\strategy.dat', Move)
	print(moves)
	print('Part 1:', sum(map(lambda x:x.score(), moves)))

	moves = parse_file('Day-2\strategy.dat', Move2)
	print(moves)
	print('Part 2:', sum(map(lambda x:x.score(), moves)))