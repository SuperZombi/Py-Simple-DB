from PySimpleDB import DataBase
tracks = DataBase("database/tracks.bd")


# ADD
def add():
	tracks.add(track=request.json['track_name'],
				artist=request.json['artist'],
				genre=request.json['genre'],
				date=request.json['date'])


# GET ROW
def get():
	track_id = tracks.find(artist=request.json['artist'], track=request.json['track_name'])
	track = tracks.get(track_id)
	return track


# GET ALL artist tracks
def get_all():
	array = tracks.find_all(artist=request.json['artist'])
	all_tracks = []
	for i in array:
		track = tracks.get(i)
		all_tracks.append(track)
	return all_tracks


# GET ALL DATA
def get_all_data():
	all_tracks = []
	for i in tracks.data:
		all_tracks.append(i)
	return all_tracks


# DELETE
def delete():
	track_id = tracks.find(artist=request.json['artist'], track=request.json['track_name'])
	tracks.delete(track_id)


# EDIT
def edit():
	track_id = tracks.find(artist=request.json['artist'], track=request.json['track_name'])
	track = tracks.get(track_id)

	track['genre'] = request.json['genre']
	tracks.save()


# Check if already exists
if tracks.find(artist=request.form['artist'], track=request.form['track_name']):
	return "track already exists"
