from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=100)
    file = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, blank=True)  # ✅ Add this line

    def __str__(self):
        return self.title