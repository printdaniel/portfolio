from django import forms
from .models import Contacto

class ConatactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ("nombre", "apellido", "email", "mensaje")

