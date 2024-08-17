import pandas as pd
from spotipy import Spotify

def get_metadata():
    
    '''
    get metadata about tracks, artists, and albums from Spotify
    
    Args:
        - idk yet
    
    Returns:
        - idk yet
    
    '''
    
    tracks_df = pd.read_csv('./data/spotify_tracks.csv')
    artists_df = pd.read_csv('./data/spotify_artists')
    albums_df = pd.read_csv('./data/spotify_albums')
    
    return tracks_df, artists_df, albums_df

def get_recent_tracks(sp: Spotify, limit=50):
    """
    get the user's recently played tracks from Spotify

    Args:
        sp (Spotify): authenticated Spotify client
        limit (int): number of tracks to fetch (max 50)

    Returns:
        dict: dictionary containing the recent track data
    """
    
    recent_tracks = sp.current_user_recently_played(limit=limit)
    return recent_tracks

def fetch_user_playlists(sp: Spotify):
    """
    get the user's playlists from Spotify

    Args:
        sp (Spotify): authenticated Spotify client

    Returns:
        dict: dictionary containing the user's playlist data
    """
    
    playlists = sp.current_user_playlists()
    return playlists
