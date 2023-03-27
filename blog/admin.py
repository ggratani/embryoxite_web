from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

#Esto es paa que aparezca en la ruta admin y permita ingresar entradas

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Categoria, CategoriaAdmin)

admin.site.register(Post, PostAdmin)