places = { }
names = "Enter your name: "
prompt = "If you could visit one place in the world, where would you go? "
active = True
while active:
	name = input(names)
	place = input(prompt)
	
	places[name] = place
	ask = input("Would you like to print enter another response? yes/no ")
	if ask == 'no':
		active = False
print("\n")
print("Here the results of the poll: ")
for name, place in places.items():
	print(name.title() + " would like to go in " + place.title() + ".")
