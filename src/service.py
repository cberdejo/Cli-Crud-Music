from sqlmodel import select
from model import Playlist, Song


def get_song_by_name_service(session,name:str):
    statement = select(Song).where(Song.name==name)
    return session.exec(statement).first()


def create_song_service(session, name: str, artist: str, duration: str, genre: str = None):
    if get_song_by_name_service(session, name) is not None:
        print("Error: Song already exits")
    else:
        try:
            # Verifica si la duración está en formato "mm:ss"
            if ":" in duration:
                minutes, seconds = map(int, duration.split(":"))
                duration_in_seconds = minutes * 60 + seconds
            else:
                # Si no contiene ":", espera que sea directamente en segundos
                duration_in_seconds = int(duration)
            
            # Crea el objeto Song
            song = Song(name=name, artist=artist, duration_seg=duration_in_seconds, genre=genre)
            
            # Agrega y guarda la canción en la base de datos
            session.add(song)
            session.commit()
        except ValueError:
            print("Error: The duration must be in the format 'mm:ss' or in seconds as a number")

def get_playlist_by_name_service(session, name:str, list[str]):
    statement = select(Playlist).where(Playlist.name==name)
    return session.exec(statement).first()  
            
def createPlaylist_service(session, playlist_name:str):
    if get_playlist_by_name_service(session, playlist_name) is not None:
        print("Error: Song already exits")
    else: 
        for song_name in songs: 
            
            
    session.commit()
