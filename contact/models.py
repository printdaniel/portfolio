from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    email = models.EmailField()
    mensaje = models.TextField()


    def __str__(self):
        return self.nombre
