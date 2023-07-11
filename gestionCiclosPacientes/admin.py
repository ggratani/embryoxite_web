from django.contrib import admin
from .models import Pacientes, Ciclos, Embrion, Dia2, Dia3, Dia5

# Register your models here.
class PacientesAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class CiclosAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class EmbrionAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class Dia2Admin(admin.ModelAdmin):
    readonly_fields=()

class Dia3Admin(admin.ModelAdmin):
    readonly_fields=()

class Dia5Admin(admin.ModelAdmin):
    readonly_fields=()

admin.site.register(Pacientes, PacientesAdmin)
admin.site.register(Ciclos, CiclosAdmin)
admin.site.register(Embrion, EmbrionAdmin)
admin.site.register(Dia2, Dia2Admin)
admin.site.register(Dia3, Dia3Admin)
admin.site.register(Dia5, Dia5Admin)