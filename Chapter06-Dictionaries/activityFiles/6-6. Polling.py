favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
people_take = ['harvey', 'jen', 'kate', 'edward', 'meriam', 'sarah']
for name in people_take:
	if name in favorite_languages.keys():
		print(name.title() + ", thank you for responding!")
	else:
		print(name.title() + ", please vote.")

