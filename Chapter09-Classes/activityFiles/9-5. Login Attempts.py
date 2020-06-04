class User():
	def __init__(self, first_name, last_name, age, location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location
		self.login_attempts = 0 # add login attempt attribute, default
		
	def describe_user(self):
		print("Full Name: " + self.first_name.title() + " " + self.last_name.title())
		print("Age: " + str(self.age))
		print("Location: " + self.location.title())
		print("\n")
		
	def greet_user(self):
		print("Hello " + self.first_name.title() + " " + self.last_name.title() + ". \nWelcome to Python!\n")
		
	def increment_login_attempts(self):
		"""Incremet the value of login attempts by 1."""
		self.login_attempts = self.login_attempts + 1 
		return self.login_attempts
		
	def reset_login_attempts(self):
		"""Reset login attempt to 0."""
		self.login_attempts = 0
	
user1 = User('harvey', 'abiagador', 17, 'butuan city')
user1.increment_login_attempts()
print(user1.login_attempts)

user1.increment_login_attempts()
print(user1.login_attempts)

user1.increment_login_attempts()
print(user1.login_attempts)

user1.increment_login_attempts()
print(user1.login_attempts)

user1.increment_login_attempts()
print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)
