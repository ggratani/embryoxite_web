from django import forms 

class FormularioEntrada(forms.Form):
    MCI = forms.IntegerField(label="Macizo celular interno", required=True)
    Trafectodermo = forms.IntegerField(label="Trafectodermo", required=True)
    GradoExpancion = forms.IntegerField(label="Grado de expanción", required=True)
    
    
class ImageForm(forms.Form):
    imagen_2 = forms.ImageField(label="Imagen dia 2", required=False)
    imagen_3 = forms.ImageField(label="Imagen dia 3", required=False)