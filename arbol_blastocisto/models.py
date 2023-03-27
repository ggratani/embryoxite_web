from django.db import models

# Create your models here.
class Imagen(models.Model):
    imagen = models.ImageField(upload_to='files/embriones', null=True, blank=True)
    titulo = "imagen-embrion"
    class Meta:
        verbose_name = 'embrion'
        verbose_name_plural = 'embriones'
    
    def __str__(self):
        return self.titulo