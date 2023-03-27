from django.contrib import admin
from .models import Imagen
# Register your models here.

class ImagenAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    
admin.site.register(Imagen)
