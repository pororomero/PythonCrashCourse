import json 
"""Ask a favorite number, then report and print it if stores previously."""
"""Otherwise, ask a user to enter his/her favorite number."""

def load_number():
	filename = 'favorite_number.json'
	with open (filename) as f_obj:
		fav_number = json.load(f_obj)
		return fav_number

def ask_number():
	filename = 'favorite_number.json'
	with open(filename, 'w') as f_obj:
		try:
			fav_number = int(input("What is your favorite number? "))
		except ValueError:
			print("Please enter a number only!")
		else:
			json.dump(fav_number, f_obj)
			return fav_number

def print_number():
		try:
			fav_number = load_number()
		except FileNotFoundError:
			fav_number = ask_number()
		print("I know your favorite number, it's " + str(fav_number) + ".")

print_number()
