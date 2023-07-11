from django.shortcuts import render
from gestionCiclosPacientes.models import Pacientes, Ciclos, Embrion
from joblib import load
import requests
import os, time, uuid, glob
from lime.lime_tabular import LimeTabularExplainer
import dill as pickle
import numpy as np

# Create your views here.
def getPatients (request):
    patients = Pacientes.objects.all()
    print("El post es este")
    print(patients)
    return render(request, "gestionCiclosPacientes/patients.html", {"patients":patients})

def getCicloDetail(request, protocolo_id):
    ciclo = Ciclos.objects.get(protocolo=protocolo_id)
    modele = load(r'C:\Users\gasto\Documents\Django\Embryoxite\arbol_blastocisto\modelos_predictivos\modelo_blastocisto_sv.joblib')
    modelb = load(r'C:\Users\gasto\Documents\Django\Embryoxite\arbol_transferidos\modelos\arbol_decision.joblib')

    paciente = ciclo.paciente  # Accede al objeto Pacientes relacionado a través de la relación Ciclos -> Pacientes
    Edad = paciente.edad

    for embrion in ciclo.embrion_set.all():
        if (embrion.dia5 is None):
            print("Entra a if")
            print(embrion.dia5)
            dia5 = 0
            Celulas_2 = embrion.dia2.cantidad_celulas
            Fragmentos_2 = embrion.dia2.porcentaje_fragmentacion
            Simetria_2 = embrion.dia2.simetria
            Celulas_3 = embrion.dia3.cantidad_celulas
            Fragmentos_3 = embrion.dia3.porcentaje_fragmentacion
            Simetria_3 = embrion.dia3.simetria
            resultado =  modele.predict([[Edad,Celulas_2,Celulas_3,Fragmentos_2,Fragmentos_3,Simetria_2,Simetria_3]])
            if resultado[0] == 1:
                embrion.transferenciabilidad = 1
            else:
                embrion.transferenciabilidad = 0
            embrion.save()
        else:
            print("Entra a Else")
            print(embrion.dia5)
            dia5 = 1
            map_dict = {"A":4, "B":3, "C":2, "D":1, " ":0}
            GradoExpancion = embrion.dia5.grado_expancion
            MCI = map_dict.get(embrion.dia5.mci)
            Trafectodermo = map_dict.get(embrion.dia5.trofoectodermo)
            resultado =  modelb.predict([[GradoExpancion, MCI, Trafectodermo]])
            if resultado[0] == 1:
                embrion.transferenciabilidad = 1
            else:
                embrion.transferenciabilidad = 0
            embrion.save()

    return render(request, "gestionCiclosPacientes/ciclos.html", {"ciclo":ciclo, "dia5":dia5})


def getEmbryoDetail1(request, embrion_id):

    embryo = Embrion.objects.get(id=embrion_id)
    paciente = embryo.ciclo.paciente  # Accede al objeto Pacientes relacionado a través de la relación Ciclos -> Pacientes
    Edad = paciente.edad
    Celulas_2 = embryo.dia2.cantidad_celulas
    Celulas_3 = embryo.dia3.cantidad_celulas
    Fragmentos_3 = embryo.dia2.porcentaje_fragmentacion
    Fragmentos_2 = embryo.dia3.porcentaje_fragmentacion
    Simetria_2 = embryo.dia2.simetria
    Simetria_3 = embryo.dia3.simetria
    # Implementación de modelo con los datos ingresados
    print(Edad)
    print(Celulas_2)
    print(Celulas_3)
    print(Fragmentos_2)
    print(Fragmentos_3)
    print(Simetria_2)
    print(Simetria_3)

    model = load(r'C:\Users\gasto\Documents\Django\Embryoxite\arbol_blastocisto\modelos_predictivos\modelo_blastocisto_sv.joblib')
    resultado =  model.predict([[Edad,Celulas_2,Celulas_3,Fragmentos_2,Fragmentos_3,Simetria_2,Simetria_3]])

    with open(r'C:\Users\gasto\Documents\Django\Embryoxite\arbol_blastocisto\modelos_predictivos\lime_model.pkl', 'rb') as file:
        explainer = pickle.load(file)
    list = [Edad,Celulas_2,Celulas_3,Fragmentos_2,Fragmentos_3,Simetria_2,Simetria_3]
    int_list = np.array([float(elem) for elem in list])
    print(int_list)
    print("----------------------------------------------------------")
    explanation = explainer.explain_instance(int_list, model.predict_proba, num_features=9)

    exp = explanation.as_html()
    exp2 = explanation.as_pyplot_figure()
    # print (exp)
    return render(request, "gestionCiclosPacientes/resultado.html", {"exp":exp, "resultado":resultado, "exp2":exp2})

def getEmbryoDetail2(request, embrion_id):

    embryo = Embrion.objects.get(id=embrion_id)
    map_dict = {"A":4, "B":3, "C":2, "D":1, " ":0}
    GradoExpancion = embryo.dia5.grado_expancion
    MCI = map_dict.get(embryo.dia5.mci)
    Trafectodermo = map_dict.get(embryo.dia5.trofoectodermo)

    model = load(r'C:\Users\gasto\Documents\Django\Embryoxite\arbol_transferidos\modelos\arbol_decision.joblib')
    resultado =  model.predict([[GradoExpancion, MCI, Trafectodermo]])

    with open(r'C:\Users\gasto\Documents\Django\Embryoxite\arbol_transferidos\modelos\lime_model_transferencia.pkl', 'rb') as file:
        explainer = pickle.load(file)
    list = [GradoExpancion, MCI, Trafectodermo]
    int_list = np.array([int(elem) for elem in list])

    # print("----------------------------------------------------------")
    explanation = explainer.explain_instance(int_list, model.predict_proba, num_features=9)

    exp = explanation.as_html()
    exp2 = explanation.as_pyplot_figure()
    # print (exp)
    return render(request, "gestionCiclosPacientes/resultado2.html", {"exp":exp, "resultado":resultado, "exp2":exp2})
