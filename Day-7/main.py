class File:
	def __init__(self, size: int):
		self.size = size

class Directory:
	def __init__(self, name: str):
		self.name = name
		self.files: list[File] = []
		self.directories: dict[str, Directory] = {}
		self.size = None
	def add_file(self, file: File):
		self.files.append(file)
	def add_dir(self, dir):
		self.directories.update({dir.name : dir})
	def get_size(self):
		size = 0
		for f in self.files:
			size += f.size
		for d in self.directories.values():
			size += d.get_size()
		self.size = size
		return size
	def repr(self, pre):
		out = f'{self.name} - {self.get_size()}\n'
		for f in self.files:
			out += pre + ' |> ' + str(f.size) + '\n'
		for d in self.directories.values():
			out += pre + ' |=>' + d.repr(pre+' |  ') + '\n'
		return out[:-2]
	def __repr__(self):
		return self.repr('')

	def collapse_dirs(self) -> list:
		dirs = [self]
		for d in self.directories.values():
			dirs.extend(d.collapse_dirs())
		return dirs


if __name__ == "__main__":
	with open('Day-7\console.dat') as file:
		contents = file.read()
	instructions = contents.split('$ ')
	instructions = map(lambda x : tuple(map(lambda z : tuple(z.split(' ')), (x.split('\n'))[:-1])), instructions)
	
	store = Directory('/')
	path = []
	current = store

	for instruction in instructions:
		if not instruction: continue
		print(instruction)
		match instruction[0][0]:
			case "ls":
				for line in instruction[1:]:
					match (line[0], line[1]):
						case ("dir", name):
							current.add_dir(Directory(name))
						case (size, name):
							current.add_file(File(int(size)))
						case _:
							print(line)
			case "cd":
				match instruction [0][1]:
					case '/':
						current = store
						path = []
					case '..':
						current = store
						if not path:
							current = store
							continue
						for part in path[:-1]:
							current = current.directories[part]
						path = path[:-1]
					case name:
						#print(path)
						#print(store)
						current = current.directories[name]
						path.append(name)
			case _:
				print('oof')

	print(store)
	all_dirs: list[Directory] = store.collapse_dirs()

	print('Part 1:',sum(map(Directory.get_size, filter(lambda d : d.get_size() <= 100000, all_dirs))))

	update_size = 30000000
	system_size = 70000000
	free_space = system_size - store.get_size()
	required_space = update_size - free_space
	print('Part 2:', min(map(Directory.get_size, filter(lambda d : d.get_size() >= required_space, all_dirs))))