from django.urls import path
from . import views

urlpatterns = [
    path('', views.getPatients, name="Analisis"),
    path('<int:protocolo_id>/', views.getCicloDetail, name="ciclo_detail"),
    path('embrion/<int:embrion_id>/', views.getEmbryoDetail1, name="embryo_detail_1"),
    path('blastocisto/<int:embrion_id>/', views.getEmbryoDetail2, name="embryo_detail_2")

]

