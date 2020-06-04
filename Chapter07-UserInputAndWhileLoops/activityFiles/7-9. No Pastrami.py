sandwich_orders = ['pocket', 'pastrami', 'bacon', 'pastrami', 'open', 'pastrami', 'british rail',]
finished_sandwiches = [ ]
print("Deli has runout of pastrami.\n")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
	print(sandwich_orders)

print("\n")
print("Here are the sandwich: ")
for sandwich_order in sandwich_orders:
	print(sandwich_order.title())
