# Exercise 7-4. 
# Use a conditional test in the while statement to stop the loop.
prompt = "Please enter your desired toppings. "
prompt += "\nEnter 'quit' if you're finished: "
toppings = " "
while toppings != 'quit':
	toppings = input(prompt)
	if toppings == 'quit':
		break
	print("I'll add " + str(toppings).title() + " to your pizza.\n")

# Use an active variable to control how long the loop runs.
prompt = "Please enter your desired toppings. "
prompt += "\nEnter 'quit' if you're finished: "
active = True
while active:
	toppings = input(prompt)
	if toppings == 'quit':
		active = False
	else:
		print("I'll add " + str(toppings).title() + " to your pizza.\n")

# Use a break statement to exit the loop when the user enters a 'quit' value.
prompt = "Please enter your desired toppings. "
prompt += "\nEnter 'quit' if you're finished: "
active = True
while active:
	toppings = input(prompt)
	if toppings == 'quit':
		active = False
		break
	else:
		print("I'll add " + str(toppings).title() + " to your pizza.\n")
