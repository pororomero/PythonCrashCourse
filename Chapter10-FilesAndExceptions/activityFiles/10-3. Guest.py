filename = 'guest.txt'

with open(filename, 'w') as file_object:
	while True:
		name = input("Input your full name, 'none' if you want to end program. \nEnter name: ")
		if name == 'none':
			break
		else:
			file_object.write(name.title() + ", You are invited.\n")
