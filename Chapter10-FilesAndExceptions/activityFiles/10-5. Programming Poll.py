filename = 'reason_programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("The reasons why people love to program: \n")
	while True:
		reason = input("Enter your reason why you love to program, \n'stop' to stop the program: ")
		file_object.write(" - " + reason + "\n")
		if reason ==  'stop':
			break
		
