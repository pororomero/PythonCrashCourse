# Returning a Dictionary
def build_person(first_name, last_name):
	"""Returns a dictionary of information about a person."""
	person =  {'first': first_name, 'last': last_name}
	return person

musician = build_person('jimi', 'hendrix')
print(musician)

# Optional age variable 
def build_person(first_name, last_name, age = ""):
	"""Returns a dictionary of information about a person."""
	person =  {'first': first_name, 'last': last_name, 'age': age}
	if age: 
		person['age'] = age
	return person
musician = build_person('jimi', 'hendrix', age = 27)
print(musician)
