import unittest

from city_functions import city_country

class NameTestCase(unittest.TestCase):
	"""Test the code it is working."""
	def test_city_country(self):
		place = city_country('santiago', 'chile')
		self.assertEqual(place, 'Santiago, Chile')
	def test_city_country_population(self):
		place = city_country('santiago', 'chile', 5000000)
		self.assertEqual(place, 'Santiago, Chile - 5000000')
		
unittest.main()
