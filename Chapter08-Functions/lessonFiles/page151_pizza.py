# Passing an arbitrary number of argument
def make_pizza(*toppings):
	"""Print the list toppings that have been requested."""
	print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# print statement with a loop
def make_pizza(*toppings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a pizza with the following toppings: ")
	for topping in toppings:
		print(" - " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
	for topping in toppings:
		print(" - " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
