"""Ask for a number then add. If the user enters string (not int), display an error using try-except block."""
print("Enter two number and I will add it. ('q' to quit.)")
while True:
	first_number = input("First Number: ")
	if first_number == 'q':
		break
	second_number = input("Second Number: ")
	if first_number == 'q':
		break
	try:
		add = int(first_number) + int(second_number)
	except ValueError:
		print("Please enter number characters only.")
	else:
		print(add)
		
