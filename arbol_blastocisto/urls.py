from django.urls import path

from . import views

urlpatterns = [
    path('', views.arbol_blastocisto, name="Arbol Blastocisto"),
    path('informacion/', views.arbol_blastocisto_info, name="Arbol Blastocisto Info"),
    path('implementacion/', views.arbol_blastocisto_implementación, name="Arbol Blastocisto Implementacion"),
    path('implementacion/resultado/', views.arbol_blastocisto_implementación_resultado, name="Arbol Blastocisto Implementacion Resultado"),

]

