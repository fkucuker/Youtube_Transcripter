# YouTube Playlist Transcript Downloader

This project downloads video transcripts from YouTube playlists and organizes them into a structured folder system. Each playlist is saved as a separate folder, and each video has its transcript stored as a `.txt` file. The transcripts do not include timestamps and are named after the video title and upload date.


![YouTube Playlist Transcript Downloader - visual selection](https://github.com/user-attachments/assets/dec5b8f1-850f-459f-bfc2-c02f2674d682)


---

## Features

1. **YouTube Playlist Handling**:
   - Extracts video information (title, ID, upload date) from each playlist.
   - Supports multiple playlists listed in the `youtube_lists.txt` file.

2. **Folder Organization**:
   - Creates a folder for each playlist, named after the playlist name.
   - Stores each video's transcript in a separate `.txt` file inside the corresponding playlist folder.

3. **Transcript Management**:
   - Fetches transcripts using YouTube's built-in transcript API if available.
   - Handles private or unavailable videos gracefully by logging the issue.

4. **File Naming and Folder Structure**:
   - Handles long titles by truncating and appending `_` to prevent file system errors.
   - Ensures compatibility with Windows file system rules (removes invalid characters).

---

## Installation

### Prerequisites
- Python 3.7 or higher
- A YouTube Data API v3 key

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/fkucuker
   cd YouTube_Project
