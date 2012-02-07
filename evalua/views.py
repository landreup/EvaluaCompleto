from django.shortcuts import render_to_response
from models import Proyecto, Usuario, Curso, Alumno
from django.http import HttpResponse, HttpResponseRedirect
from forms import CursoForm, UsuarioForm, AlumnoForm, ProyectoForm

def listadoAlumnos(request, rol):
    listaProyectos= Proyecto.objects.all()
    
    if (rol=="tutor"):
        titulo = "Alumnes Assignats"
    elif (rol=="coordinador"):
        titulo = "Gestio d'Alumnes"
    elif (rol=="coordinador-tutor"):
        rol = ["coordinador", "tutor"]
        titulo = "Alumnes de Xxxxxx Yyyyyyy Zzzzzzz"
    
    return render_to_response('listadoAlumnos.html', {'listaProyectos': listaProyectos, 'rol': rol, 'titulo': titulo})

def listadoProfesores(request):
    listaCoordinadores = Usuario.objects.filter(rol="C")
    listaTutores = Usuario.objects.filter(rol="T")
    listaProfesores = Usuario.objects.filter(rol="P")
    return render_to_response('listadoProfesores.html', {'listaCoordinadores': listaCoordinadores, 'listaTutores': listaTutores, 'listaProfesores': listaProfesores})

def listadoCursos(request):
    listaCursos = Curso.objects.all().order_by("-id")
    return render_to_response('Cursos.html', {'listaCursos': listaCursos})

def nuevoCurso(request):
    if (request.method == "POST"):
        form = CursoForm(request.POST)
        if (form.is_valid()):
            listaTutores = Usuario.objects.filter(rol="T")
            for tutor in listaTutores:
                tutor.rol="P"
                tutor.save()
            curso_nuevo = Curso(curso = form.cleaned_data['curso'])
            curso_nuevo.save()
                    
            return HttpResponseRedirect('/coordinacio/cursos')
    else:
        form = CursoForm()
        curso_actual = int(Curso.objects.order_by("-id")[0].curso.split("/")[0])
        
        form.initial["curso"] = str(curso_actual+1)+"/"+str(curso_actual+2)
    return render_to_response('CursoNuevo.html', {'form': form})

def nuevoProfesor(request):
    form = UsuarioForm()
    return render_to_response('ProfesorNuevo.html', {'form': form})

def nuevoAlumno(request):
    if (request.method == "POST") :
        form_alumno = AlumnoForm(request.POST, prefix='alumno')
        form_proyecto = ProyectoForm(request.POST, prefix='proyecto')
        if (form_alumno.is_valid() and form_proyecto.is_valid()):
            alumno = Alumno(form_alumno)
            alumno.save()
            curso = Curso.objects.order_by("-id")[0]
            proyecto = Proyecto(form_proyecto, alumno=alumno, curso=curso)
            proyecto.save()
            return HttpResponseRedirect('/coordinacio/cursos')
    else: 
        form_alumno = AlumnoForm(prefix='alumno')
        form_proyecto = ProyectoForm(prefix='proyecto')
    return render_to_response('AlumnoNuevo.html', {'form_alumno': form_alumno, 'form_proyecto': form_proyecto})

## BORRAR funcion y plantillas html   
def contact(request):
    if (request.method == "POST" ):
        form = ContactForm(request.POST)
        if (form.is_valid()):
            tema = form.cleaned_data['tema']
            mensaje = form.cleaned_data['mensaje']
            email = form.cleaned_data.get('sender', 'landreup@gmail.com')
            return render_to_response('contact_view.html', {'tema': tema, 'mensaje': mensaje, 'email': email})
    else: 
        form = ContactForm()
    return render_to_response('contact.html', {'form': form})