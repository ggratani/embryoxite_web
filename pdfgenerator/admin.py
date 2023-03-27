from django.contrib import admin
from .models import Postpdf

# Register your models here.

#Esto es paa que aparezca en la ruta admin y permita ingresar entradas


class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')



admin.site.register(Postpdf, PostAdmin)