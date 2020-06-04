def open_text(filename):
	with open(filename) as file_object:
		print("The following are the names of animals: ")
		contents = file_object.readlines()
		for content in contents:
			print(" - " + content.rstrip())
		print("\n")

filenames = ['cats.txt', 'dogs.txt']
try:
	for filename in filenames:
		open_text(filename)
except FileNotFoundError:
	pass
	
