def show_magicians(magicians):
	for magician in magicians:
		print(magician.title())
		
def make_great(magicians):
	for magician in magicians:
		greet = magician.title() + " the Great"
		print(greet) 

magicians = ['harvey', 'meriam', 'mercy']
show_magicians(magicians)
make_great(magicians[:])

# NOT WORKING/FINISHED
