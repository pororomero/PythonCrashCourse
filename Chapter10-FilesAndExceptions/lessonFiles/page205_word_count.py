def word_count(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		pass
		"""msg = "Sorry, the file " + filename + " does not exist."
		print(msg)""" # <- to execute something after the try function fails, pass - to ignore and continue, do nothing
	else:
		# count the approximate number of words in the file.
		words = contents.split()
		number_words = len(words)
		print("The file " + filename + " has about " + str(number_words) + " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	word_count(filename)
