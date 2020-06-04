import json


def ask_new():
	username = get_stored_username()
	ask = input("Is " + username + " your username? yes/no : ")
	if ask == 'yes':
		greet_user()
	else:
		get_new_username()

def get_stored_username():
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""Prompt for a new username.""" 
	filename = 'username.json'
	username = input("What is your name? ")
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
		print("Well remember you when you come back, " + username + "!")
	return username

def greet_user():
	"""Greet user by name."""
	username = get_stored_username()
	if username:
		print("Welcome back, " + username + "!")
	else:
		username = get_new_username()
		

ask_new()
