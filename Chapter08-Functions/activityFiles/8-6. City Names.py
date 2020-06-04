def city_country(city, country):
	location = '"' + city.title() + ", " + country + '"'
	return location

location = city_country('Santiago', 'Chile')  
print(location)
location = city_country('Butuan', 'Philippines')
print(location)
location = city_country('Cagayan De Oro', 'Philippines')
print(location)
