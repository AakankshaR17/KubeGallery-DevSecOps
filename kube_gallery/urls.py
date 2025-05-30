from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gallery/', include('gallery.urls', namespace='gallery')),
    path('upload/', include('gallery.urls', namespace='gallery')),  # Optional
    path('', RedirectView.as_view(url='/gallery/', permanent=False)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)