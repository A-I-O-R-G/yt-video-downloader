import os
from pytube import Channel
import argparse

def download_videos(channel_url, num_videos, download_path, file_format):
    """Faz o download dos vídeos do canal especificado."""
    try:
        channel = Channel(channel_url)

        print(f"Baixando os últimos {num_videos} vídeos do canal: {channel.channel_name}")

        videos_to_download = channel.videos[:num_videos]

        for video in videos_to_download:
            print(f"Baixando: {video.title}")
            # Verifica o formato solicitado
            if file_format == 'mp4':
                stream = video.streams.get_highest_resolution()
            else:
                stream = video.streams.filter(file_extension=file_format).first()
            
            if stream:
                stream.download(output_path=download_path)
                print(f"Download concluído: {video.title}")
            else:
                print(f"Formato não encontrado para: {video.title}")
        
    except Exception as e:
        print(f"Ocorreu um erro durante o download: {e}")

def main():
    # Parser de argumento
    parser = argparse.ArgumentParser(description='Baixador de vídeos do YouTube.')
    parser.add_argument('channel_url', type=str, help='URL do canal do YouTube')
    parser.add_argument('-n', '--num_videos', type=int, default=5, help='Número de vídeos a serem baixados (padrão: 5)')
    parser.add_argument('-d', '--download_path', type=str, default=os.getcwd(), help='Diretório de download (padrão: diretório atual)')
    parser.add_argument('-f', '--format', type=str, choices=['mp4', 'webm'], default='mp4', help='Formato do vídeo (padrão: mp4)')

    # Processa os argumentos
    args = parser.parse_args()

    # Faz o download dos vídeos
    download_videos(args.channel_url, args.num_videos, args.download_path, args.format)

if __name__ == "__main__":
    main()