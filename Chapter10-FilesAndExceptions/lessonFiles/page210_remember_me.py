import json

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f_obj:
	json.dump(username, f_obj)
	print("Well remember you when you come back, " + username + "!")
	
