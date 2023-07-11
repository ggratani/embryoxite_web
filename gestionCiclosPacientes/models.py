from django.db import models
import uuid

# Create your models here.
class Pacientes(models.Model):
    nombre=models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    edad = models.IntegerField()
    email = models.EmailField()
    telefono= models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'paciente'
        verbose_name_plural = 'pacientes'
    
    def __str__(self):
        return self.nombre

class Ciclos(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE, related_name='ciclos')
    protocolo = models.CharField(max_length = 10)
    tecnica = models.CharField(max_length = 10)
    transferido = models.BooleanField()
    nacimiento = models.BooleanField()
    cancelado = models.BooleanField()
    embarazo_bioquimico = models.BooleanField()
    embarazo_clinico = models.BooleanField()
    embarazo_multiple = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'ciclo'
        verbose_name_plural = 'ciclos'
    
    def __str__(self):
        return self.protocolo
    
class Dia2(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cantidad_celulas = models.IntegerField()
    porcentaje_fragmentacion = models.FloatField()
    simetria = models.BooleanField()

    class Meta:
        verbose_name = 'dia2'
        verbose_name_plural = 'dias2'
    
    def __str__(self):
        return str(self.id)

class Dia3(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cantidad_celulas = models.IntegerField()
    porcentaje_fragmentacion = models.FloatField()
    simetria = models.BooleanField()

    class Meta:
        verbose_name = 'dia3'
        verbose_name_plural = 'dias3'
    
    def __str__(self):
        return str(self.id)
    
class Dia5(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    blastocisto = models.BooleanField()
    grado_expancion = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')))
    mci = models.CharField(max_length=1, choices=(('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')))
    trofoectodermo = models.CharField(max_length=1, choices=(('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')))

    class Meta:
        verbose_name = 'dia5'
        verbose_name_plural = 'dias5'
    
    def __str__(self):
        return str(self.id)

class Embrion(models.Model):
    id = models.AutoField(primary_key=True)
    ciclo = models.ForeignKey(Ciclos, on_delete=models.CASCADE)
    transferenciabilidad = models.BooleanField()
    dia2 = models.ForeignKey(Dia2, on_delete=models.CASCADE, null=True, blank=True)
    dia3 = models.ForeignKey(Dia3, on_delete=models.CASCADE, null=True, blank=True)
    dia5 = models.ForeignKey(Dia5, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'embrion'
        verbose_name_plural = 'embriones'
    
    def __str__(self):
        return str(self.id)

