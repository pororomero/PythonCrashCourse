words_meaning = {'int': 'The int() method returns an integer object from any number or string.', 
				 'str': 'The str() method returns the "informal" or nicely printable representation of a given object.', 
				 'float': 'The float() method returns a floating point number from a number or a string.', 
				 'print': 'The print() function prints the specified message to the screen, or other standard output device.', 
				 'return': 'The return statement causes your function to exit and hand back a value to its caller.',
}
print("int: " + words_meaning['int'] + "\n")
print("str: " + words_meaning['str'] + "\n")
print("float: " + words_meaning['float'] + "\n")
print("print: " + words_meaning['print'] + "\n")
print("return: " + words_meaning['return'] + "\n")

word = input("Enter a word: ")
if word == "int":
	print(words_meaning['int'])
if word == "str":
	print(words_meaning['int'])
if word == "float":
	print(words_meaning['int'])
if word == "print":
	print(words_meaning['print'])
if word == "return":
	print(words_meaning['return'])
