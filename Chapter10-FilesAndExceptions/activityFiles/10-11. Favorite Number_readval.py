import json

"""Read and print the favorite number entered by the user."""
filename = 'favorite_number.json'

with open (filename) as f_obj:
	fav_number = json.load(f_obj)
	print("I know your favorite number, it's " + str(fav_number) + ".")
