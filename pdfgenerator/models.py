from django.db import models
from django.contrib.auth.models import User



class Postpdf(models.Model):
    titulo = models.CharField(max_length=500, blank=True)
    contenido = models.CharField(max_length=500, null=True, blank=True)
    imagen = models.ImageField(upload_to = 'blog', null=True, blank=True) 
    descripcion = models.CharField(max_length=5000, null=True, blank=True) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'postpdf'
        verbose_name_plural = 'postpdfs'
    
    def __str__(self):
        return self.titulo