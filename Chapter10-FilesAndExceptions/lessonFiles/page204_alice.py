filename = 'alice.txt'

try:
	with open(filename) as file_object:
		contents = file_object.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)
else:
	# count the approximate number of words in the file.
	words = contents.split()
	number_words = len(words)
	print("The file " + filename + " has about " + str(number_words) + " words.")
