import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


def authentication():
    client_id = os.environ['SPOTIFY_CLIENT_ID']
    client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
    auth = HTTPBasicAuth(username=client_id, password=client_secret)

    url = "https://accounts.spotify.com/api/token"
    body = {
        'grant_type': 'client_credentials',
    }
    answer = requests.post(url=url, data=body, auth=auth)

    try:
        answer.raise_for_status()
    except requests.HTTPError as e:
        print(f"request fail : {e}")
        token = None
    else:
        token = answer.json()['access_token']
    return token



def search_artist(name_artist , headers):
    url = "https://api.spotify.com/v1/search"
    params ={
        'q' :name_artist,
        'type':'artist',
    }
    answer = requests.get(url, params=params, headers=headers)
    try:
        first_result = answer.json()['artists']['items'][0]
    except IndexError:
        first_result = None
    return first_result


def search_top_musics(id_artist, headers):
    url = f"https://api.spotify.com/v1/artists/{id_artist}/top-tracks"
    answer = requests.get(url, headers=headers)
    return answer.json()['tracks']



def main():
    st.title('Web App Spotify')
    st.write('Spotify API Doc (https://developer.spotify.com/documentation/web-api)')
    name_artist = st.text_input('search artist:')
    if not name_artist:
        st.stop()

    token = authentication()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    artist = search_artist(name_artist=name_artist,headers=headers)
    if not artist:
        st.warning(f'artist not found ! (search:{name_artist})')
        st.stop()

    
    id_artist = artist['id']
    name_artist = artist['name']
    popularity_artist = artist['popularity']

    best_musics = search_top_musics(id_artist=id_artist, headers=headers)

    st.subheader(f' artist : {name_artist} (pop: {popularity_artist})')

    for music in best_musics :
        music_name = music['name']
        music_popularity = music['popularity']
        music_link = music['external_urls']['spotify']
        markdown_link = f'[{music_name}]({music_link})'
        st.write(f'{markdown_link} (pop: {music_popularity}) ')

if __name__ == '__main__':

    main()
