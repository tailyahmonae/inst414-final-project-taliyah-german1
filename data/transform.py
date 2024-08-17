import difflib

def filter_tracks_by_artist(tracks, artist_name):
    """
    Filters tracks by the specified artist name.
    
    Args:
        tracks (list): List of track dictionaries, each containing metadata such as 'artist'.
        artist_name (str): The artist name to filter by.
        
    Returns:
        list: Filtered list of tracks where the artist matches the specified name.
    """
    filtered_tracks = [track for track in tracks if track['artist'].lower() == artist_name.lower()]
    return filtered_tracks

def filter_tracks_by_genre(tracks, genre):
    """
    Filters tracks by the specified genre.
    
    Args:
        tracks (list): List of track dictionaries, each containing metadata such as 'genre'.
        genre (str): The genre to filter by.
        
    Returns:
        list: Filtered list of tracks where the genre matches the specified genre.
    """
    filtered_tracks = [track for track in tracks if genre.lower() in [g.lower() for g in track.get('genres', [])]]
    return filtered_tracks

def find_similar_tracks(tracks, track_name, similarity_threshold=0.7):
    """
    Finds tracks that are similar to the specified track name using string similarity.
    
    Args:
        tracks (list): List of track dictionaries, each containing metadata such as 'track_name'.
        track_name (str): The name of the track to find similar tracks to.
        similarity_threshold (float): A threshold to determine how similar tracks need to be. Defaults to 0.7.
        
    Returns:
        list of tracks that are similar to the specified track name.
    """
    similar_tracks = []
    
    for track in tracks:
        similarity = difflib.SequenceMatcher(None, track['track_name'].lower(), track_name.lower()).ratio()
        if similarity >= similarity_threshold:
            similar_tracks.append(track)
    
    return similar_tracks
