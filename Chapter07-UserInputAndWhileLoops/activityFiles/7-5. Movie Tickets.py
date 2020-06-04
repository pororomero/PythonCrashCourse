age = int(input("Please enter your age to continue: "))
if age < 3:
	print("The ticket costs free.")
if 3 <= age <= 12:
	print("The ticket costs $10.")
elif age > 12:
	print("The ticket costs $15.")
	
