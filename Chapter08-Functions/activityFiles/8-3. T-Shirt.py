def make_shirt(size, text):
	size = str(size)
	print( text + " will be printed in T-Shirt size " + size + ".")

make_shirt(20, "'Red Raptors'") # <- Call using positional argument
make_shirt(size = 20, text = "'Red Raptors'") # <- Call using keyword argument 
