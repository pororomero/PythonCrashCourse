"""Ask for a number then add. If the user enters string (not int), display an error using try-except block."""
print("Enter two number and I will add it.")
first_number = input("First Number: ")
second_number = input("Second Number: ")
try:
	add = int(first_number) + int(second_number)
except ValueError:
	print("Please enter number characters only.")
else:
	print(add)
		
