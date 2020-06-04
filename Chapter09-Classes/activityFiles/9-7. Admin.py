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
		print("\n")
		
	def greet_user(self):
		print("Hello " + self.first_name.title() + " " + self.last_name.title() + ". \nWelcome to Python!\n")
		
class Admin(User):
	def __init__(self, first_name, last_name, age, location):
		super().__init__(first_name, last_name, age, location)
		self.privileges = [ ] 
		
	def show_privileges(self):
		print("These are the privileges of an Administrator: ")
		for privilege in privileges:
			print(" - " + privilege.title())
	
user1 = User('meriam', 'lauzon', 24, 'butuan city')
user2 = User('mercy', 'abiagador', 45, 'butuan city')
admin1 = Admin('harvey', 'abiagador', 17, 'butuan city')
admin1.privileges = ['can add post', 'can delete post', 'can ban user']
admin1.show_privileges()

# NOT DEFINED/WORKING 
