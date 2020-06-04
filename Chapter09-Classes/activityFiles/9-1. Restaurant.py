class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	def describe_restaurant(self):
		print("Name of Restaurant: " + self.restaurant_name.title())
		print("Cuisine Type: " + self.cuisine_type.title())
	def open_restaurant(self): 
		print("The " + self.restaurant_name.title() + " restaurant is now open.")

restaurant = Restaurant('grand palace', 'buffet')
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title() + "\n")
restaurant.describe_restaurant()
restaurant.open_restaurant()
