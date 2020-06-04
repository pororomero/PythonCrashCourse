harvey = {'first_name': 'harvey', 'last_name': 'abiagador', 'age': '17', 'city': 'butuan city',}
meriam = {'first_name': 'meriam', 'last_name': 'lauzon', 'age': '24', 'city': 'butuan city'}
mercy = {'first_name': 'mercy', 'last_name': 'abiagador', 'age': '46', 'city': 'butuan city'}
proceso = {'first_name': 'proceso', 'last_name': 'abiagador', 'age': '45', 'city': 'butuan city'}
mitchie = {'first_name': 'mitchie', 'last_name': 'abiagador', 'age': '13', 'city': 'butuan city'}

people = [harvey, meriam, mercy]
for name in people:
	print("Name: " + name['first_name'].title() + " " + name['last_name'].title())
	print("Age: " + name['age'].title())
	print("City: " + name['city'].title() + "\n")
