def common_words(filename):
	with open(filename, encoding="utf8") as file_object:
		contents = file_object.read()
		the = contents.lower().count('the')
		print(the)
		
filenames = ['the_blind_musician.txt', 'sherlock_holmes.txt']
for filename in filenames:
	common_words(filename)
