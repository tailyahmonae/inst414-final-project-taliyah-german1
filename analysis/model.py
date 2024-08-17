def generate_playlist_based_on_history(sp, user_id, track_ids, playlist_name="Generated Playlist"):
    """
    generate a new playlist based on the user's listening history.

    Args:
        sp (Spotify): authenticated Spotify client
        user_id (str): Spotify user ID
        track_ids (list of str): list of track IDs to add to the new playlist
        playlist_name (str): name of the playlist to create

    Returns:
        dict: new playlist data
    """
    
    new_playlist = sp.user_playlist_create(user_id, playlist_name, public=False)
    sp.playlist_add_items(new_playlist['id'], track_ids)
    return new_playlist

