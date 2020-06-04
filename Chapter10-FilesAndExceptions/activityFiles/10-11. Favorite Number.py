import json

"""Ask a user for its favorite number."""
filename = 'favorite_number.json'

with open(filename, 'w') as f_obj:
	try:
		fav_number = int(input("What is your favorite number? "))
	except ValueError:
		print("Please enter a number only!")
	else:
		json.dump(fav_number, f_obj)
