def make_album(artist_name, album_title, num_tracks = ""):
	album = {}
	album[artist_name] = album_title
	if num_tracks:
		album['# of Track'] = num_tracks
	return album

jason = make_album('Jason Derulo', 'Everything is 4')
print(jason)
meghan = make_album('Meghan Trainor', 'Title')
print(meghan)
maroon5 = make_album('Maroon 5', "It Won't Be Soon Before Long")
print(maroon5)
adele = make_album('Adele', 'Greatest Hits', '20')
print(adele)
