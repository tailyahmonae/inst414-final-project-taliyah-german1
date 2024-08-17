def evaluate_playlist(tracks, criteria, value):
    """
    evaluate the playlist based on given criteria

    Args:
        tracks (list): list of track objects
        criteria (str): criteria for evaluation (e.g., genre, artist, similar tracks)
        value (str): value for the criteria

    Returns:
        float: evaluation score
    """
    
    if criteria == 'genre':
        score = sum([1 for track in tracks if value in track.get('genres', [])]) / len(tracks)
    elif criteria == 'artist':
        score = sum([1 for track in tracks if value in track.get('artists', [])]) / len(tracks)
    elif criteria == 'similarity':
        score = sum([1 for track in tracks if value in track.get('similar_tracks', [])]) / len(tracks)
    return score
