from django.db import models
from django.core.exceptions import ValidationError

def validate_media_count(media):
    if media.count() > 5:
        raise ValidationError("No se pueden agregar más de 5 imágenes/videos.")

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    MEDIA_CHOICES = [('image', 'Image'), ('video', 'Video')]
    media_type = models.CharField(max_length=20, choices=MEDIA_CHOICES)
    
    def __str__(self):
        return self.title

class ProjectMedia(models.Model):
    project = models.ForeignKey(Project, related_name='media', on_delete=models.CASCADE, validators=[validate_media_count])
    media_type = models.CharField(max_length=20, choices=Project.MEDIA_CHOICES)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Media for {self.project.title}"
