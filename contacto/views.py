from django.shortcuts import render, redirect
from .forms import FormularioContacto

from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    formulario_contacto = FormularioContacto()
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            print(email)
            email = EmailMessage("Mensaje desde app Embryoxite", "El usuario {} con la direccion {} escribe: \n\n {}".format(nombre,email, contenido),
            "",[email], reply_to=["gastongratani@hotmail.com"])

            try:
                email.send()
                return redirect("/contacto/?valido")

            except:
                return redirect("/contacto/?novalido")

    return render(request, "contacto/contacto.html", {"miformulario":formulario_contacto})