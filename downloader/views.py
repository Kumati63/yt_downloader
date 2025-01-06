import yt_dlp
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt
def get_media_info(request):
    if request.method == "GET":
        media_url = request.GET.get('url', '')

        if not media_url:
            return JsonResponse({'error': 'URL is required'}, status=400)

        # Nueva configuración de yt-dlp sin FFmpeg
        ydl_opts = {
            'format': 'bestaudio/bestvideo',  # Mejor calidad de audio y video
            'noplaylist': True,               # No descargar playlists
            'quiet': True,                    # Modo silencioso
            'outtmpl': 'downloads/%(id)s.%(ext)s',  # Ruta de salida
        }
        
        try:
            # Intentamos extraer la información del video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(media_url, download=False)

                # Si no hay formato, devolvemos un error
                formats = info_dict.get('formats', [])
                if not formats:
                    return JsonResponse({'error': 'No formats found for the media'}, status=404)

                # Filtrar calidades de video
                allowed_resolutions = ['144p', '240p', '360p', '480p', '720p', '1080p', '720p60', '1080p60', '1440p', '2160p', '4320p']
                filtered_video_formats = [
                    {"quality": f['format_note'], "url": f['url']}
                    for f in formats if 'format_note' in f and 'url' in f and f['format_note'] in allowed_resolutions and f['vcodec'] != 'none'
                ]

                # Filtrar calidades de audio, excluyendo "storyboard", "medium", y "unknown quality"
                filtered_audio_formats = [
                    {"quality": f.get('format_note', 'Unknown quality'), "url": f['url']}
                    for f in formats if 'url' in f and 'acodec' in f and f.get('format_note') == 'medium'
                    # Excluir otros formatos con "storyboard", "low", etc.
                ]


                # Evitar duplicados en las calidades de video
                unique_video_formats = {f['quality']: f for f in filtered_video_formats}
                filtered_video_formats = list(unique_video_formats.values())

                # Evitar duplicados en las calidades de audio
                unique_audio_formats = {f['quality']: f for f in filtered_audio_formats}
                filtered_audio_formats = list(unique_audio_formats.values())

                # Devolver la información al frontend
                media_info = {
                    "title": info_dict.get('title', 'No title found'),
                    "thumbnail": info_dict.get('thumbnail', ''),
                    "video_formats": filtered_video_formats,
                    "audio_formats": filtered_audio_formats
                }

                return JsonResponse(media_info)

        except yt_dlp.utils.DownloadError as e:
            return JsonResponse({'error': f'yt-dlp error: {str(e)}'}, status=500)
        except Exception as e:
            return JsonResponse({'error': f'Unexpected error: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def index(request):
    return render(request, 'downloader/index.html')
