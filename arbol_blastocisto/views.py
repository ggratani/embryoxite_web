from django.shortcuts import render, redirect
from .forms import FormularioEntrada, ImageForm
from .models import Imagen
from joblib import load
import requests
import os, time, uuid, glob
from PIL import Image, ImageDraw
from .funciones import count_cells

from lime.lime_tabular import LimeTabularExplainer
import dill as pickle
import numpy as np

# Create your views here.
def arbol_blastocisto(request):
    return render(request, "arbol_blastocisto/base.html")

def arbol_blastocisto_info(request):
    return render(request, "arbol_blastocisto/informacion.html")

def arbol_blastocisto_implementación(request):
    return render(request, "arbol_blastocisto/implementacion.html")

def arbol_blastocisto_implementación(request):
    
    #Endpoint servicio azure
    ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/82561cf1-aae3-4a88-aec4-b0d0d7d8f099/detect/iterations/Iteration1/image"
    prediction_key = "65419bbf42a14489baee0e89a6fd7d36"

    headers = {"Content-Type": "application/octet-stream", "Prediction-Key":prediction_key}
    ############################

    formulario_entrada = FormularioEntrada()
    image_form = ImageForm()
    imagenes = {}
    resultado = "Pending"
    cwd = os.getcwd()

    # if request.method=="GET":
    #     if resultado == "Pending":
    #         try:
    #             os.remove(cwd + '\\media\\files\\embriones\\' + "imagen2_guardada.jpg")
    #             os.remove(cwd + '\\media\\files\\embriones\\' + "imagen3_guardada.jpg")
    #         except: 
    #             pass

    # Si se presiona boton enviar
    if request.method=="POST":
        # Leo datos ingresados
        formulario_entrada=FormularioEntrada(data=request.POST)
        if formulario_entrada.is_valid():
            Edad = request.POST.get("Edad")
            Celulas_2 = request.POST.get("Celulas_2")
            Celulas_3 = request.POST.get("Celulas_3")
            Fragmentos_2 = request.POST.get("Fragmentos_2")
            Fragmentos_3 = request.POST.get("Fragmentos_3")
            Simetria_2 = request.POST.get("Simetria_2")
            Simetria_3 = request.POST.get("Simetria_3")
            Ovulo_donante = request.POST.get("Ovulo_donante")
            Semen_donante = request.POST.get("Semen_donante")
            email="gastongratani@hotmail.com"
            print(Simetria_2)
            print(Simetria_3)
            print(Ovulo_donante)
            print(Semen_donante)
            Semen_donante = 1 if Semen_donante == "on" else 0 
            Ovulo_donante = 1 if Ovulo_donante == "on" else 0 
            Simetria_2 = 1 if Simetria_2 == "on" else 0
            Simetria_3 = 1 if Simetria_3 == "on" else 0
            
            return redirect(f"/modelos/arbol_blastocisto/implementacion/resultado/?Edad={Edad}&Celulas_2={Celulas_2}&Celulas_3={Celulas_3}&Fragmentos_2={Fragmentos_2}&Fragmentos_3={Fragmentos_3}&Ovulo_donante={Ovulo_donante}&Semen_donante={Semen_donante}&Simetria_2={Simetria_2}&Simetria_3={Simetria_3}")

        
        # Leo imagenes de entrada
        image_form = ImageForm(data=request.POST)
        if image_form.is_valid():
            image_form = ImageForm(data=request.POST)
                       
            # De esta manera se obtienen las imagenes de forms de django
            imagen_2 = request.FILES.get("imagen_2")
            if imagen_2:
                img_2_db = Imagen.objects.create(imagen = imagen_2)
                img_2_db.save()
                image2_url = cwd + img_2_db.imagen.url.replace("/","\\")
                image_2 = Image.open(image2_url)
                with open(image2_url, "rb") as image_contents:
                    data = image_contents.read()
                    response = requests.post(ENDPOINT, headers=headers, data=data)
                    data = response.json()
                    cont2 = count_cells(data, image_2)
                image_2.save(cwd + '\\media\\files\\embriones\\' + "imagen2_guardada.jpg")

            imagen_3 = request.FILES.get("imagen_3")
            if imagen_3:
                img_3_db = Imagen.objects.create(imagen = imagen_3)
                img_3_db.save()
                image3_url = cwd + img_3_db.imagen.url.replace("/","\\")
                image_3 = Image.open(image3_url)           
                with open(image3_url, "rb") as image_contents:
                    data = image_contents.read()
                    response = requests.post(ENDPOINT, headers=headers, data=data)
                    data = response.json()
                    cont3 = count_cells(data, image_3)
                image_3.save(cwd + '\\media\\files\\embriones\\' + "imagen3_guardada.jpg")

            imagenes["imagen_2"] = '/media/files/embriones/' + "imagen2_guardada.jpg"
            imagenes["imagen_3"] = '/media/files/embriones/' + "imagen3_guardada.jpg"

            formulario = FormularioEntrada()
            formulario.initial={'Celulas_2': cont2, "Celulas_3":cont3}

            print(formulario)
            return render(request, "arbol_blastocisto/implementacion.html", {"miformulario":formulario, "imageform":image_form, "resultado":resultado, "imagenes":imagenes})
 
    return render(request, "arbol_blastocisto/implementacion.html", {"miformulario":formulario_entrada, "imageform":image_form, "resultado":resultado, "imagenes":imagenes})

def arbol_blastocisto_implementación_resultado(request):

    if request.method=="GET":
        Edad = request.GET.get("Edad")
        Celulas_2 = request.GET.get("Celulas_2")
        Celulas_3 = request.GET.get("Celulas_3")
        Fragmentos_3 = request.GET.get("Fragmentos_3")
        Fragmentos_2 = request.GET.get("Fragmentos_2")
        Ovulo_donante = request.GET.get("Ovulo_donante")
        Semen_donante = request.GET.get("Semen_donante")
        Simetria_2 = request.GET.get("Simetria_2")
        Simetria_3 = request.GET.get("Simetria_3")
    # Implementación de modelo con los datos ingresados
    print(Simetria_2)
    print(Simetria_3)
    print(Ovulo_donante)
    print(Semen_donante)
    model = load(r'C:\Users\gasto\Documents\Django\Embryoxite\arbol_blastocisto\modelos_predictivos\arbol_profundidad5.joblib')
    resultado =  model.predict([[Edad,Celulas_2,Celulas_3,Fragmentos_2,Fragmentos_3,Ovulo_donante,Semen_donante,Simetria_2,Simetria_3]])

    with open(r'C:\Users\gasto\Documents\Django\Embryoxite\arbol_blastocisto\modelos_predictivos\lime_model.pkl', 'rb') as file:
        explainer = pickle.load(file)
    list = [Edad,Celulas_2,Celulas_3,Fragmentos_2,Fragmentos_3,Ovulo_donante,Semen_donante,Simetria_2,Simetria_3]
    int_list = np.array([int(elem) for elem in list])

    print("----------------------------------------------------------")
    explanation = explainer.explain_instance(int_list, model.predict_proba, num_features=9)

    exp = explanation.as_html()
    exp2 = explanation.as_pyplot_figure()
    # print (exp)
    return render(request, "arbol_blastocisto/resultado.html", {"exp":exp, "resultado":resultado, "exp2":exp2})
