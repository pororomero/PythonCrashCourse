# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed models after printing.
while unprinted_designs:
	current_design = unprinted_designs.pop()
	
	# Simulate creating a 3D print from the design.
	print("Printing Model: " + current_design)
	completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed: ")
for completed_model in completed_models:
	print(completed_model)
	
# VERSION 2 - MAKING 2 FUNCTIONS
def print_models(unprinted_designs, completed_models):
	# Simulate printing each design, until none are left.
	# Move each design to completed models after printing.
	while unprinted_designs:
		current_design = unprinted_designs.pop()
	
		# Simulate creating a 3D print from the design.
		print("Printing Model: " + current_design)
		completed_models.append(current_design)	

def show_completed_models(completed_models):
	print("\nThe following models have been printed: ")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models) # <- [:] only sends a copy not the original list
show_completed_models(completed_models)
# print(unprinted_designs) # <- to prove [:]
