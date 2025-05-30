from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.image_gallery, name='image_gallery'),
    path('upload/', views.upload, name='upload'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('edit/<int:image_id>/', views.edit_caption, name='edit_caption'),
]