cities = {'butuan': {
			'country': 'philippines',
			'population': '10,000',
			'fact': 'It is where the first mass in the country happened.',
			}, 
		  'cabadbaran': {
			'country': 'philippines',
			'population': '15,000',
			'fact': 'The last to become city in the CARAGA region.',
		    }, 
		  'cagayan de oro': {
			'country': 'philippines',
			'population': '20,0000',
			'fact': 'It was devastated by Bagyong Pablo last 2014.',
		    },
		
}
for city, info in cities.items():
	print("Name: " + city.title())
	print("Country: " + info['country'].title())
	print("Population: " + info['population'].title())
	print("Fact: " + info['fact'] + "\n")
	
