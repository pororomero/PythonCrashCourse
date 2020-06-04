class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	def describe_restaurant(self):
		print("Name of Restaurant: " + self.restaurant_name.title())
		print("Cuisine Type: " + self.cuisine_type.title())
	def open_restaurant(self): 
		print("The " + self.restaurant_name.title() + " restaurant is now open.")

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = []
		
	def display_flavors(self):
		print("The flavors are: ")
		for flavor in self.flavors:
			 print(" - " + flavor.title())
	
restaurant = Restaurant('grand palace', 'buffet')

ic_stand = IceCreamStand('grand palace', 'buffet')
ic_stand.flavors = ['mango', 'chocolate', 'cheese']
ic_stand.display_flavors()
