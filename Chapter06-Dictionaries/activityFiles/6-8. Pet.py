brownie = {'name': 'brownie', 'kind': 'dog', 'owner': 'harvey'}
whitie = {'name': 'whitie','kind': 'cat', 'owner': 'meriam'}
blackie = {'name': 'blackie','kind': 'rabbit', 'owner': 'mercy'}

pets = [brownie, whitie, blackie]
for pet in pets:
	print("Name: " + pet['name'].title())
	print("Kind: " + pet['kind'].title())
	print("Owner: " + pet['owner'] +"\n")
	
