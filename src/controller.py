from service import create_song_service


def create_song_controller(session, arguments):
    print("Creating song")
    parameters= arguments.split("|")
    
    if len(parameters) == 3:
        name,artist,duration = parameters
        genre = None
    elif len(parameters) == 4:
        name,artist,duration,genre = parameters
    else:
        print("Error: The application expects: name|artist|duration|genre(optional)")
        return
    create_song_service(session,name,artist,duration,genre)

def create_playlist_controller(session,arguments):
    print("Creating playlist. Playlist name = ", arguments)
    playlist, *songs = arguments.split("|")
    
    create_playlist_service(session,playlist,songs)