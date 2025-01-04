from utils import sanitize_filename, sanitize_date
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from tqdm import tqdm
from pytube import YouTube
import os
import whisper
import subprocess

# Whisper modeli yükleniyor
model = whisper.load_model("base")

def download_transcripts(video_data, transcripts_dir, playlist_name):
    playlist_folder = os.path.join(transcripts_dir, sanitize_filename(playlist_name))
    if not os.path.exists(playlist_folder):
        os.makedirs(playlist_folder)

    # Liste adı ile log dosyalarına başlık ekle
    with open("success_log.txt", "a", encoding="utf-8") as success_log:
        success_log.write(f"\n=== SUCCESS LOG: {playlist_name} ===\n")
    with open("error_log.txt", "a", encoding="utf-8") as error_log:
        error_log.write(f"\n=== ERROR LOG: {playlist_name} ===\n")

    for video in tqdm(video_data, desc=f"Downloading Transcripts for {playlist_name}"):
        clean_title = sanitize_filename(video["title"], max_length=40)
        clean_date = sanitize_date(video["date"])
        file_name = f"{clean_title} - {clean_date}.txt"
        file_path = os.path.join(playlist_folder, file_name)

        transcript_text = None
        method = None

        try:
            # Öncelikle "en" dil kodunda transkripti dene
            transcript = YouTubeTranscriptApi.get_transcript(video["id"], languages=['en'])
            transcript_text = "\n".join([t["text"] for t in transcript])
            method = "YouTube Transcript (en)"
        except (TranscriptsDisabled, NoTranscriptFound):
            print(f"No transcript available for {video['title']} - Using Whisper")
            try:
                # Whisper kullanarak transkript oluştur
                audio_path = download_audio_yt_dlp(video["id"], clean_title)
                whisper_transcript = generate_transcript_with_whisper(audio_path)
                transcript_text = whisper_transcript
                method = "Whisper Transcript"
            except Exception as e:
                print(f"Error processing {video['title']} with Whisper: {e}")
                log_error(video["title"], str(e), playlist_name)
                continue
        except Exception as e:
            print(f"Unexpected error for {video['title']}: {e}")
            log_error(video["title"], str(e), playlist_name)
            continue

        # Transkripti dosyaya yaz ve log kaydı yap
        if transcript_text:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(transcript_text)
            print(f"Transcript downloaded successfully for {video['title']}")
            log_success(video["title"], method, playlist_name)

def download_audio(video_id, title):
    youtube_url = f"https://www.youtube.com/watch?v={video_id}"
    yt = YouTube(youtube_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    output_path = "temp_audio"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    audio_file = audio_stream.download(output_path, filename=f"{sanitize_filename(title)}.mp4")
    return audio_file



def download_audio_yt_dlp(video_id, title):
    youtube_url = f"https://www.youtube.com/watch?v={video_id}"
    output_path = "temp_audio"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    output_file = os.path.join(output_path, f"{sanitize_filename(title)}.mp3")
    command = [
        "yt-dlp",
        "-x", "--audio-format", "mp3",
        "--output", output_file,
        youtube_url
    ]
    subprocess.run(command, check=True)
    return output_file



def generate_transcript_with_whisper(audio_path):
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")
    result = model.transcribe(audio_path)
    os.remove(audio_path)  # Geçici dosyayı sil
    return result["text"]


def log_success(video_title, method, playlist_name):
    """
    Saves successful transcript transactions.
    """
    with open("success_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"{playlist_name} - SUCCESS: {video_title} - Method: {method}\n")

def log_error(video_title, error_message, playlist_name):
    """
    Saves failed transactions.
    """
    with open("error_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"{playlist_name} - ERROR: {video_title} - Error: {error_message}\n")
