words_meaning = {'int': 'The int() method returns an integer object from any number or string.', 
				 'str': 'The str() method returns the "informal" or nicely printable representation of a given object.', 
				 'float': 'The float() method returns a floating point number from a number or a string.', 
				 'print': 'The print() function prints the specified message to the screen, or other standard output device.', 
				 'return': 'The return statement causes your function to exit and hand back a value to its caller.',
}
for word, meaning in words_meaning.items():
	print(word.title() + ": " + meaning)
