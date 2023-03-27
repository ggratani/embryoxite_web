from django.shortcuts import render, redirect

from pdfgenerator.models import Postpdf

# Create your views here.

def generar_pdf(request):
    posts = Postpdf.objects.all()
    return render(request, "pdf_generator/body.html", {"posts":posts})