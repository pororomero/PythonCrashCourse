
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.\n")
while True:
	first_number = input("First Number: ")
	if first_number == 'q':
		break
	second_number = input("Second Number: ")
	if second_number == 'q':
		break
	try:	
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't a number by zero!")
	else:
		print(answer)
