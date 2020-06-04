number = "Enter a number, and I'll tell you if it's a multiple of 10. "
number += "\nNumber: "
number = int(input(number))

if number % 10 == 0:
	print("It is a multiple of 10.")
else: 
	print("It is not a multiple of 10.")
