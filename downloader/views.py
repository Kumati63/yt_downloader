import yt_dlp
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt  # Solo si es necesario para pruebas, idealmente usa CSRF en producción
def get_video_info(request):
    if request.method == "GET":
        video_url = request.GET.get('url', '')

        if not video_url:
            return JsonResponse({'error': 'URL is required'}, status=400)

        ydl_opts = {
            'format': 'bestaudio/bestvideo',
            'noplaylist': True,
            'quiet': True,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # Extraer solo los metadatos sin descargar el video
                info_dict = ydl.extract_info(video_url, download=False)
                formats = info_dict.get('formats', [])

                # Filtrar solo las opciones con un formato válido
                video_info = {
                    "title": info_dict.get('title'),
                    "thumbnail": info_dict.get('thumbnail'),
                    "formats": [{"quality": f['format_note'], "url": f['url']} for f in formats if f.get('format_note') and f.get('url')]
                }

                return JsonResponse(video_info)

        except Exception as e:
            return JsonResponse({'error': f'Error extracting video information: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

# Vista principal para renderizar el formulario
def index(request):
    return render(request, 'downloader/index.html')
