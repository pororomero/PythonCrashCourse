# print the entire file
filename = 'learning_python.txt'

with open(filename) as file_object:
	learned = file_object.read()
	print(learned)

filename = 'learning_python.txt'

# print by looping ove the file object
with open(filename) as file_object:
	learned = file_object.readlines()
	for learning in learned:
		print(learning.strip())

filename = 'learning_python.txt'

# print by storing lines in a list
with open(filename) as file_object:
	learned = file_object.readlines()
	learned = ''
	for learning in learned:
		print(learning.strip())
	learned += learning
print(learned)
