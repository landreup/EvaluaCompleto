from django import forms
from models import Curso, Usuario, Alumno, Proyecto
from django.forms import ModelForm

TOPIC_CHOICES = (
                 ('g', "General"),
                 ('e', "Informacio d'errors"),
                 ('s', "Sugerencias")
                 )
class ContactForm(forms.Form):
    tema = forms.ChoiceField(choices=TOPIC_CHOICES)
    mensaje = forms.CharField(widget=forms.Textarea(),
                              initial="Escribe tu opinion")
    email = forms.EmailField(required=False)

class CursoForm(ModelForm):
    class Meta():
        model = Curso
        
class UsuarioForm(ModelForm):
    class Meta():
        model = Usuario
        
class AlumnoForm(ModelForm):
    class Meta():
        model = Alumno  

class ProyectoForm(ModelForm):
    class Meta():
        model = Proyecto
        exclude = ('curso', 'alumno')