class Car():
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + " " + self.make.title() + " " + self.model.title()
		return long_name
	
	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
		
	def update_odometer(self, mileage):
		"""Set the odometer reading to the given table"""
		"""Reject the change it it attempts to roll the odometer back."""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back the odometer")
			
	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles
		
class ElectricCar(Car):
	"""Represents aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class."""
		"""Then initialize attributes specific to an electric cars."""
		super().__init__(make, model, year)
		
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# Defining attributes and methods for the child class.
class Car():
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + " " + self.make.title() + " " + self.model.title()
		return long_name
	
	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
		
	def update_odometer(self, mileage):
		"""Set the odometer reading to the given table"""
		"""Reject the change it it attempts to roll the odometer back."""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back the odometer")
			
	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles
		
class ElectricCar(Car):
	"""Represents aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class."""
		"""Then initialize attributes specific to an electric cars."""
		super().__init__(make, model, year)
		self.battery_size = 70
	
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
		
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.describe_battery()

# Overriding Methods from the Parent class.
class Car():
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + " " + self.make.title() + " " + self.model.title()
		return long_name
	
	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
		
	def update_odometer(self, mileage):
		"""Set the odometer reading to the given table"""
		"""Reject the change it it attempts to roll the odometer back."""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back the odometer")
			
	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles
		
	def fill_gas_task():
		"""Cars that need a gas tank."""
		print("This car needs a gas tank.")
		
class ElectricCar(Car):
	"""Represents aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class."""
		"""Then initialize attributes specific to an electric cars."""
		super().__init__(make, model, year)
		self.battery_size = 70
	
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
		
	def fill_gas_task():
		"""Electric cars don't have a gas tanks."""
		print("This car don't need a gas tank!")
		
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.describe_battery()

# Instances as attribute
class Car():
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + " " + self.make.title() + " " + self.model.title()
		return long_name
	
	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
		
	def update_odometer(self, mileage):
		"""Set the odometer reading to the given table"""
		"""Reject the change it it attempts to roll the odometer back."""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back the odometer")
			
	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles
		
	def fill_gas_task():
		"""Cars that need a gas tank."""
		print("This car needs a gas tank.")
		
class Battery():
	"""A simple attempt to model a battery for an electric car."""
	def __init__(self, battery_size=70):
		self.battery_size = battery_size
	
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
	
	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		
		message = "This car can go approxiamtely " + str(range)
		message += " miles on a full charge."
		print(message)
	
class ElectricCar(Car):
	"""Represents aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class."""
		"""Then initialize attributes specific to an electric cars."""
		super().__init__(make, model, year)
		self.battery = Battery()		
		
	def fill_gas_task():
		"""Electric cars don't have a gas tanks."""
		print("This car don't need a gas tank!")
		

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
