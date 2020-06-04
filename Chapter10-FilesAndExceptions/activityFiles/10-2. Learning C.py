# print the entire file
filename = 'learning_python.txt'

with open(filename) as file_object:
	learned = file_object.read()
	learned_c = learned.replace('python', 'c')
	print(learned_c)
