from typing import Optional
from sqlmodel import Field, SQLModel

class Playlist(SQLModel, table=True):
    name:str = Field(primary_key=True)
   

class Song(SQLModel, table=True):
    name: str = Field(primary_key=True)
    duration_seg:int = Field(gt=0)
    genre:str | None
    artist:str

class SongInPLaylist(SQLModel, table=True):
    playlist: Playlist = Field(primary_key=True, foreign_key="playlist.name"),
    song:Song = Field(primary_key=True, foreign_key="song.name")