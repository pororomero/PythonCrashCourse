def greeter_user():
	"""Display a simple greeting."""
	print("Hello! ")

greeter_user()

# Passing Information to a Function
def greeter_user(username):
	"""Display a simple greeting."""
	print("Hello! " + username.title() + ".")

greeter_user('jesse')
