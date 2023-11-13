from django import forms

class AfiliacionFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=100)
    apellido = forms.CharField(required=True, max_length=100)
    dni = forms.CharField(required=True, max_length=10)
    telefono = forms.CharField(required=True, max_length=20)
    email = forms.CharField(required=True, max_length=32)
    fecha_de_nacimiento = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    direccion = forms.CharField(required=True, max_length=50)
    plan_choices = [(100, 'Plan 100'), (200, 'Plan 200'), (300, 'Plan 300')]
    plan = forms.ChoiceField(choices=plan_choices, widget=forms.Select())