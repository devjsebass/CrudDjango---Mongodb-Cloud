from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages

# Create your views here.

def home(request):
    cursosListados = Curso.objects.all()
    #messages.success(request, '¡Cursos listados correctamente!')
    return render(request, "gestionCursos.html", {"cursos": cursosListados})

def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(codigo = codigo, nombre = nombre, creditos = creditos)
    messages.success(request, '¡Curso registrado correctamente!')
    return redirect('/')

def editarCurso(request, codigo):
    curso = Curso.objects.get(codigo = codigo)
    return render(request, "editarCurso.html", {"curso": curso})

def actualizarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo = codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    messages.success(request, '¡Curso actualizado correctamente!')
    return redirect('/')


def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo = codigo)
    curso.delete()

    messages.success(request, '¡Curso eliminado correctamente!')
    return redirect('/')
    