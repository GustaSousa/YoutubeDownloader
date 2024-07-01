import ssl
import certifi
from pytube import YouTube
import os
import ffmpeg
import socket

# Configura o contexto SSL para usar o CA Bundle do certifi
ssl._create_default_https_context = ssl._create_unverified_context

def download_video(url):
    try:
        # Cria um objeto YouTube
        yt = YouTube(url)
        
        # Seleciona o stream de vídeo com a maior resolução
        video_stream = yt.streams.filter(file_extension='mp4').order_by('resolution').desc().first()
        
        # Baixa o vídeo com a melhor resolução
        print(f"Baixando vídeo: {yt.title}")
        video_file_path = video_stream.download(filename='video')
        video_file_path_with_extension = video_file_path + '.' + video_stream.mime_type.split('/')[1]
        os.rename(video_file_path, video_file_path_with_extension)
        print(f"Download do vídeo concluído: {yt.title}")
        
        # Seleciona a faixa de áudio
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        # Baixa a faixa de áudio em formato MP3
        print(f"Baixando áudio: {yt.title}")
        audio_file_path = audio_stream.download(filename='audio')
        audio_file_path_with_extension = audio_file_path + '.' + audio_stream.mime_type.split('/')[1]
        os.rename(audio_file_path, audio_file_path_with_extension)
        print(f"Download do áudio concluído: {yt.title}")
        
        return yt.title, video_file_path_with_extension, audio_file_path_with_extension
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
        output_file = f"{title}.mp4"
        merge_video_audio(video_file, audio_file, output_file)
    else:
        print("Falha ao baixar vídeo ou áudio.")