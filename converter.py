import os
import yt_dlp

def baixar_video_youtube(url, pasta_destino):
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,  # Extrai apenas o áudio
        'audioformat': 'mp3',  # Converte para MP3
        'outtmpl': os.path.join(pasta_destino, '%(title)s.%(ext)s'),  # Salva como MP3
        'postprocessors': [{  # Adiciona um pós-processador para converter para MP3
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Baixando: {url}")
        ydl.download([url])

def main():
    url = input("Digite a URL do vídeo do YouTube: ")
    pasta_destino = input("Digite o caminho da pasta onde deseja salvar o MP3: ")

    os.makedirs(pasta_destino, exist_ok=True)

    baixar_video_youtube(url, pasta_destino)
    print("Download e conversão concluídos! Verifique a pasta especificada.")

if __name__ == "__main__":
    main()

