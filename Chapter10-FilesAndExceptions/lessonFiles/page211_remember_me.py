import json

# Load the username, if it has been stores previously.
# Otherwise, prompt for the username and store it.

filename = 'username.json'
try:
	with open(filename) as f_obj:
		username = json.load(f_obj)

except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
		print("Well remember you when you come back, " + username + "!")
	
else:
	print("Welcom back, " + username + "!")
