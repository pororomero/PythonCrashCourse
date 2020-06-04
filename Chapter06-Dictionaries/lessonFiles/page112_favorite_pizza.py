favorite_languages  = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
	print(name.title() + "'s favorite programming languages are: ")
	for language in languages:
		print("\t" + language.title())
	print("\n")

# are to is if language < 1 	
for name, languages in favorite_languages.items():
	if len(languages) > 1:
		print(name.title() + "'s favorite programming languages are: ")
		for language in languages:
			print("\t" + language.title())
	else:
		print(name.title() + "'s favorite programming language is: ")
		for language in languages:
			print("\t" + language.title())
	print("\n")
		
