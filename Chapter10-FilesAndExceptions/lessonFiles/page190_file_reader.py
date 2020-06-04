"""Open pi_digits.txt with Python."""
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip()) #<- rstrip() to remove empty lines

# File Paths (relative)
"""Open pi_digits.txt with Python."""
with open('text_files\pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip()) #<- rstrip() to remove empty lines
	
# File Paths (absolute)
"""Open pi_digits.txt with Python."""
file_path = r'C:\Users\Harvey L. Abiagador\HARVEY\PROGRAMMING LANGUAGES\Python\python_works\my works from books\Eric Matthes - Python\Chapter 10 - Files and Exceptions\lessonFiles\pi_digits.txt'
with open(file_path) as file_object:
	contents = file_object.read()
	print(contents.rstrip()) #<- rstrip() to remove empty lines
	
# Reading a file line by line 
filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

# Making a list of lines from a file.
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
	
for line in lines:
	print(line.rstrip())

# Working with a File's Content
filename = 'pi_digits.txt'

with open(filename) as file_objects:
	lines = file_objects.readlines()
	
pi_string = ''
for line in lines:
	pi_string += line.strip() # <- rstrip() remove empty lines, strip() remove whitespacee on the left side 
	
print(pi_string)
print(len(pi_string))
