sandwich_orders = ['pocket', 'bacon', 'open', 'british rail',]
finished_sandwiches = [ ]

while sandwich_orders:
	sandwich_order = sandwich_orders.pop()
	
	print("I made your " + sandwich_order.title() + ".")
	finished_sandwiches.append(sandwich_order)
print("\n")
print("Here are the sandwich: ")
for finished_sandwich in finished_sandwiches:
	 print(finished_sandwich.title())
