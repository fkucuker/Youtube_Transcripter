from Youtube_Transcripter.fetch_videos import fetch_videos_from_playlist
from Youtube_Transcripter.download_transcripts import download_transcripts
import os

if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY"

    # Set the path to the playlist file relative to the project directory
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Current script directory
    playlist_file_path = os.path.join(base_dir, "youtube_lists.txt")

    # Directory for saving transcripts
    transcripts_dir = os.path.join(base_dir, "transcripts")
    os.makedirs(transcripts_dir, exist_ok=True)  # Ensure the directory exists

    # Fetch video data from playlists
    video_data = fetch_videos_from_playlist(API_KEY, playlist_file_path)

    # Download transcripts for each playlist
    for playlist in video_data:  # video_data is a list, so we can iterate directly
        playlist_name = playlist.get("playlist_name")  # Name of the playlist
        videos = playlist.get("videos")  # List of videos in this playlist
        download_transcripts(videos, transcripts_dir, playlist_name)
