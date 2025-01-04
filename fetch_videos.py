from googleapiclient.discovery import build

def fetch_videos_from_playlist(api_key, playlist_file):
    youtube = build("youtube", "v3", developerKey=api_key)
    playlists_data = []

    with open(playlist_file, "r") as file:
        playlists = file.readlines()

    for playlist_url in playlists:
        playlist_id = playlist_url.split("list=")[-1].strip()
        playlist_name = f"Playlist_{playlist_id[:10]}"  # Playlist adını belirlemek
        videos = []

        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=50
        )

        while request:
            response = request.execute()
            for item in response["items"]:
                video_title = item["snippet"]["title"]
                video_id = item["snippet"]["resourceId"]["videoId"]
                upload_date = item["snippet"]["publishedAt"]
                videos.append({
                    "title": video_title,
                    "id": video_id,
                    "date": upload_date
                })
            request = youtube.playlistItems().list_next(request, response)

        playlists_data.append({
            "playlist_name": playlist_name,
            "videos": videos
        })

    return playlists_data
