class User():
	def __init__(self, first_name, last_name, age, location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location
		
	def describe_user(self):
		print("Full Name: " + self.first_name.title() + " " + self.last_name.title())
		print("Age: " + str(self.age))
		print("Location: " + self.location.title())
		
	def greet_user(self):
		print("Hello " + self.first_name.title() + " " + self.last_name.title() + ". \nWelcome to Python!\n")
		
	
user1 = User('harvey', 'abiagador', 17, 'butuan city')
user2 = User('meriam', 'lauzon', 24, 'butuan city')
user3 = User('mercy', 'abiagador', 45, 'butuan city')
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
