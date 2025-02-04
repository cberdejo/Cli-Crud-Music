from ast import arguments
from sqlmodel import Session
import streamlit as st 

from main import create_song, create_playlist, list_playlists, get_available_songs, init_db,db_engine

st.title("Music App") 
st.write("Welcome to the music app. You can create songs and playlists.")
st.subheader("Options")

@st.cache_resource
def connect_db(): 
    init_db()
    return Session(db_engine)
    
db_session = connect_db()

if st.button("Create Song"):
    song_name = st.text_input("Song Name")
    duration = st.slider("Duration", 0, 1000)
    artist = st.text_input("Artist")
    genre = st.text_input("Genre (optional)")
    if st.button("Save"):
        create_song(db_session, song_name, artist, duration, genre)
        st.write("Song created successfully")
st.divider()
if st.button("Create Playlist"):
    playlist_name = st.text_input("Playlist Name")
    songs = get_available_songs(db_session)
    songs_multiselect = st.multiselect("Songs", [song.name for song in songs])
    if st.button("Save"):
        create_playlist(db_session, playlist_name, songs)
        st.write("Playlist created successfully")
st.divider()
if st.button("List Playlists"):
    playlists = list_playlists(db_session)
    for playlist in playlists:
        st.write(playlist.name)