prompt = "Please enter your desired toppings. "
prompt += "\nEnter 'quit' if you're finished: "
toppings = " "
while toppings != 'quit':
	toppings = input(prompt)
	if toppings == 'quit':
		break
	print("I'll add " + str(toppings).title() + " to your pizza.\n")
