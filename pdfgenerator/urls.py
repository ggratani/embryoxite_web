from django.urls import path

from . import views

urlpatterns = [
    path('', views.generar_pdf, name="generar_pdf"),
]

