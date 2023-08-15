from django.shortcuts import render
from .forms import ConatactoForm


def contact(request):
    data = {
            'form': ConatactoForm()
            }

    if request.method== 'POST':
        formulario = ConatactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Datos Registradios"
        else:
            data["form"] = formulario

    return render(request, 'contact.html', data)
