class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
		
	def describe_restaurant(self):
		print("Name of Restaurant: " + self.restaurant_name.title())
		print("Cuisine Type: " + self.cuisine_type.title())
		
	def open_restaurant(self): 
		print("The " + self.restaurant_name.title() + " restaurant is now open.")
		
	def set_number_served(self, number_served):
		self.number_served = number_served
	
	def increment_number_served(self, customer_day):
		self.number_served += customer_day
	
	
restaurant = Restaurant('grand palace', 'buffet')
print("Customers Served: " + str(restaurant.number_served))
restaurant.number_served = 20
print("Customers Served: " + str(restaurant.number_served))

restaurant.set_number_served(30)
print("Customers Served: " + str(restaurant.number_served))

restaurant.increment_number_served(10)
print("Customers Served: " + str(restaurant.number_served))
