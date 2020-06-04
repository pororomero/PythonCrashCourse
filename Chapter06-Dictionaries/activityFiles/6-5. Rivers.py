rivers = {'nile': 'egypt', 'sepik': 'new guinea','volga': 'russia'}
for river, place in rivers.items():
	print("The " + river.title() + " runs through " + place.title() + ".")

for river in rivers.keys():
	print(river.title())
	
for place in rivers.values():
	print(place.title())
