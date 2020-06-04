filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
	file_object.write("People who will visit the place: \n")
	while True:
		name = input("Enter your name if you want to visit, \n'none' to stop the program: ")
		if name != 'none':
			file_object.write(" - " + name.title() + "\n")
			print(name.title() + " will visit the place.")
		else:
			break
