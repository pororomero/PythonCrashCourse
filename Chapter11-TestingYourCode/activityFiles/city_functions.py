
def city_country(city, country, population=''):
	if population:
		place = city + ", " + country + " - " + str(population)
	else:
		place = city + ", " + country
	return place.title()
