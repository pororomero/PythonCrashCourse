# Positional Argument 
def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print("I have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".\n")

describe_pet('hamster', 'harry')

# Multiple Function Calls
def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print("I have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".\n")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Keyword Arguments
def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print("I have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".\n")

describe_pet(animal_type = 'hamster', pet_name = 'harry')

# Default Value 
def describe_pet(pet_name, animal_type = 'dog'):
	"""Display information about a pet."""
	print("I have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".\n")

describe_pet('harry', 'hamster')

# Avoiding argument errors.
def describe_pet(pet_name, animal_type):
	"""Display information about a pet."""
	print("I have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".\n")

describe_pet() # <- arguments should be provided!
