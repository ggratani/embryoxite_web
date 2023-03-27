from django import forms 

class FormularioEntrada(forms.Form):
    Edad = forms.IntegerField(label="Edad del paciente", required=True)
    Celulas_2 = forms.IntegerField(label="Cantidad de células", required=True)
    Fragmentos_2 = forms.IntegerField(label="% de fragmentación", required=True)
    Simetria_2 = forms.BooleanField(label="Presenta simetría?", required=False)
    Celulas_3 = forms.IntegerField(label="Cantidad de células", required=True)
    Fragmentos_3 = forms.IntegerField(label="% de fragmentación", required=True)
    Simetria_3 = forms.BooleanField(label="Presenta simetría?", required=False)
    Ovulo_donante = forms.BooleanField(label="Óvulo de donante?", required=False)
    Semen_donante = forms.BooleanField(label="Semen de donante?", required=False)
    
class ImageForm(forms.Form):
    imagen_2 = forms.ImageField(label="Imagen dia 2", required=False)
    imagen_3 = forms.ImageField(label="Imagen dia 3", required=False)