from django.urls import path

from . import views

urlpatterns = [
    path('', views.arbol_transferidos, name="Arbol Transferidos"),
    path('informacion/', views.arbol_transferidos_info, name="Arbol Transferidos Info"),
    path('implementacion/', views.arbol_transferidos_implementación, name="Arbol Transferidos Implementacion"),
    path('implementacion/resultado/', views.arbol_transferidos_implementación_resultado, name="Arbol Transferidos Implementacion Resultado"),
]


