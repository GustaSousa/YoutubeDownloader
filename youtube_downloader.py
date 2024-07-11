import ssl
import yt_dlp as youtube_dl
import os
import ffmpeg
import socket
import re

# Configura o contexto SSL para usar o CA Bundle do certifi
ssl._create_default_https_context = ssl._create_unverified_context

def sanitize_filename(filename):
    """Remove caracteres especiais para criar um nome de arquivo seguro."""
    return re.sub(r'[^\w\s-]', '', filename).strip().replace(' ', '_')

def download_video(url):
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }]
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url, download=False)
            title = result.get('title', None)
            sanitized_title = sanitize_filename(title)

            # Baixa o vídeo e áudio
            print(f"Baixando vídeo e áudio: {title}")
            ydl.download([url])

            video_file = f"{sanitized_title}.mp4"
            audio_file = f"{sanitized_title}.m4a"

            # Renomeia os arquivos baixados
            if os.path.exists(f"{title}.mp4"):
                os.rename(f"{title}.mp4", video_file)
            if os.path.exists(f"{title}.m4a"):
                os.rename(f"{title}.m4a", audio_file)

            return sanitized_title, video_file, audio_file
    except youtube_dl.DownloadError as e:
        print(f"Ocorreu um erro ao baixar o vídeo: {e}")
        return None, None, None
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None, None, None

def merge_video_audio(video_path, audio_path, output_path):
    try:
        # Usa ffmpeg para juntar vídeo e áudio
        input_video = ffmpeg.input(video_path)
        input_audio = ffmpeg.input(audio_path)
        ffmpeg.output(input_video, input_audio, output_path, vcodec='copy', acodec='aac').run()
        print(f"Merged video and audio saved as: {output_path}")
    except ffmpeg.Error as e:
        print(f"Error merging video and audio: {e}")

if __name__ == "__main__":
    url = input("Digite a URL do vídeo do YouTube: ").strip()
    
    # Verifica a conectividade com o YouTube
    try:
        socket.create_connection(("www.youtube.com", 80))
    except OSError:
        print("Falha ao conectar ao YouTube. Verifique sua conexão de internet.")
        exit(1)
    
    title, video_file, audio_file = download_video(url)
    
    if video_file and audio_file:
        output_file = f"{title}_merged.mp4"
        merge_video_audio(video_file, audio_file, output_file)
    else:
        print("Falha ao baixar vídeo ou áudio.")