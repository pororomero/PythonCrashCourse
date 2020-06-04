# Creating a Dog class
class Dog():
	""" A simple attempt to model a dog """
	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age 
	
	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(self.name.title() + " is now sitting.")
		
	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + " rolled over!")
		
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " year's old.")

# Calling methods
my_dog.sit()
my_dog.roll_over()

# Creating multiple instances
your_dog = Dog('lucy', 3)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " year's old.")
your_dog.sit()
my_dog.roll_over()
 
