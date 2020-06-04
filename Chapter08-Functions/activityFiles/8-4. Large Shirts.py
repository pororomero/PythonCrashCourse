def make_shirt(size = "'large'", text = "'I love Python'"):
	print(text + " will be printed in T-Shirt size " + size.title() + ".")
	
make_shirt() # <- default size and message
make_shirt(size = 'medium') # <- size changed to medium with default message
make_shirt(size = 'medium', text = "'C is the next language I love'")
	
