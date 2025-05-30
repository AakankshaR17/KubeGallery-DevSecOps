from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Image
from django.utils import timezone

def image_gallery(request):
    images = Image.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery/gallery.html', {'images': images})

@csrf_exempt
def upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        title = request.POST.get('title', '').strip()
        file = request.FILES['file']
        category = request.POST.get('category', '').strip()
        image = Image.objects.create(
            title=title,
            file=file,
            category=category,
            uploaded_at=timezone.now()
        )
        return JsonResponse({'status': 'success', 'data': {'title': image.title, 'filename': image.file.name}})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

@csrf_exempt
def delete_image(request, image_id):
    try:
        image = Image.objects.get(id=image_id)
        image.delete()
        return JsonResponse({'status': 'success'})
    except Image.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Image not found'}, status=404)

@csrf_exempt
def clear_all_images(request):
    Image.objects.all().delete()
    return JsonResponse({'status': 'success', 'message': 'All images deleted'})

@csrf_exempt
def edit_caption(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    if request.method == 'POST':
        new_caption = request.POST.get('caption', '').strip()
        if new_caption:
            image.caption = new_caption
            image.uploaded_at = timezone.now()
            image.save()
            return JsonResponse({'status': 'success', 'message': 'Caption updated'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Caption cannot be empty'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)