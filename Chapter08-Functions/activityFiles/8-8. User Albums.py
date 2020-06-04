def make_album(artist_name, album_title, num_tracks = ""):
	album = {}
	album[artist_name] = album_title
	if num_tracks:
		album['# of Track'] = num_tracks
	return album
while True:	
	artist_name = input("Enter the artist: ")
	album_title = input("Enter his/her album: ")
	num_tracks = input("Enter the number of tracks (optional): ")
	album = make_album(artist_name.title(), album_title.title(), num_tracks)
	print(album)
	ask = input("Do you want to enter another entry? yes/no: ")
	if ask == 'no':
		break
	
