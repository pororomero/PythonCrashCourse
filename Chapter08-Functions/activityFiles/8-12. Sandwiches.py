def accept_sandwich(*wants):
	print("The sandwich that is being ordered: ")
	for want in wants:
		print(" - " + want)
	print("\n")
accept_sandwich('bacon', 'smoked salmon salad', 'garlic mayo')
accept_sandwich('beets', 'spinach', 'goat cheese')
accept_sandwich('roast pork', 'pickled cucumber')
