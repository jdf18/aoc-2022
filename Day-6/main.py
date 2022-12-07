# class Queue:
# 	def __init__(self, length=10000):
# 		self.data = [None]* length
# 		self.start_pointer = 0
# 		self.end_pointer = 0
# 		self.length = 0
# 	def queue(self, data):
# 		self.data[self.end_pointer] = ord(data)
# 		self.end_pointer += 1
# 		self.length += 1
# 	def dequeue(self):
# 		data = self.data[self.start_pointer]
# 		self.start_pointer += 1
# 		self.length -= 1
# 		return data
# 	def contents(self):
# 		return self.data[self.start_pointer : self.end_pointer]


if __name__ == "__main__":
	# with open('Day-6\signal.dat') as file:
	# 	contents = file.read().strip()
	# q = Queue()
	# found_marker = False
	# marker_index = None
	# for i, char in enumerate(contents):
	# 	q.queue(char)
	# 	if not found_marker:
	# 		if q.length == 4:
	# 			con = q.contents()
	# 			if len(con) == len(set(con)):
	# 				found_marker = True
	# 				marker_index = q.end_pointer
	# 			q.dequeue()
	# 		else:
	# 			pass
		
	# 	else:
	# 		if q.length == 14:
	# 			con = q.contents()
	# 			if len(con) == len(set(con)):
	# 				message_index = q.start_pointer 
	# 			q.dequeue()
	# 		else:
	# 			pass
	# print("Part 1:", marker_index)
	# print("Part 2:", message_index)
	# #print(contents[message_index-10 : message_index + 20])
	# #print('          |')


	with open('Day-6\signal.dat') as file:
		contents = file.read().strip()

	for j in range(len(contents) - 4):
		if len(set(contents[j:j+4])) == 4:
			print('Part 1:', j+4)
			break

	for j in range(len(contents) - 14):
		if len(set(contents[j:j+14])) == 14:
			print('Part 2:', j+14)
			break


