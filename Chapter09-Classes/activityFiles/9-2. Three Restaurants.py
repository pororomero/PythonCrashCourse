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

# Add another 3 restaurant
restaurant1 = Restaurant('budget foods', 'eat all you can')
restaurant2 = Restaurant('lg mega','buffet')
restaurant3 = Restaurant("rosario's sea food",'eat all you can')
print("\n")
restaurant1.describe_restaurant()
print("\n")
restaurant2.describe_restaurant()
print("\n")
restaurant3.describe_restaurant()

