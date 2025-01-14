import os
from argparse import  ArgumentParser
from sqlmodel import Session, SQLModel, create_engine, select
from dotenv import load_dotenv

from controller import create_playlist_controller, create_song_controller
from model import Song, Playlist, SongInPLaylist

load_dotenv(override=True)


db_engine = None
db_url = os.getenv("DATABASE_URL")
db_debug_flag = bool(os.getenv("DEBUG", False))


def init_db():
    """Database initialization function."""
    global db_engine
    db_engine = create_engine(db_url, echo=db_debug_flag)
    SQLModel.metadata.create_all(db_engine)

def execute_command(arguments, session):
    if arguments.create_playlist is not None:
        create_playlist_controller(session,arguments.create_playlist)

    elif arguments.create_song is not None:
        create_song_controller(session,arguments.create_song)


    elif arguments.list_playlists is not None:
        print("3")
        pass 
    else: 
        print("Unknown command, use -h for help")



def main():

    parser = ArgumentParser(
                    prog='music-lib',
                    description='Application create and delete playlists, add songs to playlist, and view a all the playlists and songs added to your music collection.',
                    epilog='')
    parser.add_argument("-p","--create_playlist", help='playlist name', required=False)
    parser.add_argument("-c", "--create_song", help='name|artist|duration|genre(optional)', required=False)
    parser.add_argument("-l", "--list_playlists", required=False, action='store_true')

    arguments = parser.parse_args()
    init_db()
    global db_engine

    with Session (db_engine) as session:
        execute_command(arguments, session)
    

if __name__ == "__main__":
    main()

