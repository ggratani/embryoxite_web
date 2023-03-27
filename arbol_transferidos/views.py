from django.shortcuts import render, redirect
from .forms import FormularioEntrada, ImageForm
from .models import Imagen
from joblib import load
import requests
import os, time, uuid, glob
from PIL import Image, ImageDraw

from lime.lime_tabular import LimeTabularExplainer
import dill as pickle
import numpy as np

# Create your views here.
def arbol_transferidos(request):
    return render(request, "arbol_transferidos/base.html")

def arbol_transferidos_info(request):
    return render(request, "arbol_transferidos/informacion.html")

def arbol_transferidos_implementación(request):
    return render(request, "arbol_transferidos/implementacion.html")

def arbol_transferidos_implementación(request):
    
    formulario_entrada = FormularioEntrada()
    image_form = ImageForm()
    imagenes = {}
    resultado = "Pending"
    cwd = os.getcwd()

    # Si se presiona boton enviar
    if request.method=="POST":
        # Leo datos ingresados
        formulario_entrada=FormularioEntrada(data=request.POST)
        if formulario_entrada.is_valid():
            MCI = request.POST.get("MCI")
            Trafectodermo = request.POST.get("Trafectodermo")
            GradoExpancion = request.POST.get("GradoExpancion")
                        
            return redirect(f"/modelos/arbol_transferidos/implementacion/resultado/?MCI={MCI}&Trafectodermo={Trafectodermo}&GradoExpancion={GradoExpancion}")
 
    return render(request, "arbol_transferidos/implementacion.html", {"miformulario":formulario_entrada,  "resultado":resultado})

def arbol_transferidos_implementación_resultado(request):

    if request.method=="GET":
        MCI = request.GET.get("MCI")
        Trafectodermo = request.GET.get("Trafectodermo")
        GradoExpancion = request.GET.get("GradoExpancion")

    model = load(r'C:\Users\gasto\Documents\Django\Embryoxite\arbol_transferidos\modelos\arbol_decision.joblib')
    resultado =  model.predict([[GradoExpancion, MCI, Trafectodermo]])

    with open(r'C:\Users\gasto\Documents\Django\Embryoxite\arbol_transferidos\modelos\lime_model.pkl', 'rb') as file:
        explainer = pickle.load(file)
    list = [GradoExpancion, MCI, Trafectodermo]
    int_list = np.array([int(elem) for elem in list])

    # print("----------------------------------------------------------")
    explanation = explainer.explain_instance(int_list, model.predict_proba, num_features=9)

    exp = explanation.as_html()
    exp2 = explanation.as_pyplot_figure()
    # print (exp)
    return render(request, "arbol_transferidos/resultado.html", {"exp":exp, "resultado":resultado, "exp2":exp2})
