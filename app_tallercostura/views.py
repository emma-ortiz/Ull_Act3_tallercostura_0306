
from django.shortcuts import render, redirect, get_object_or_404

from .models import Alumno
from django.urls import reverse
from django.utils import timezone



def inicio_tallercostura(request):

    return render(request, 'inicio.html')



def agregar_alumno(request):

    if request.method == 'POST':

        nombre = request.POST['nombre']

        apellido = request.POST['apellido']

        correo = request.POST['correo']

        telefono = request.POST['telefono']

        direccion = request.POST['direccion']

        fecha_nacimiento = request.POST['fecha_nacimiento']

        Alumno.objects.create(

            nombre=nombre,

            apellido=apellido,

            correo=correo,

            telefono=telefono,

            direccion=direccion,

            fecha_nacimiento=fecha_nacimiento

        )

        return redirect('ver_alumno')

    return render(request, 'alumno/agregar_alumno.html')



def ver_alumno(request):

    alumnos = Alumno.objects.all()

    return render(request, 'alumno/ver_alumno.html', {'alumnos': alumnos})



def actualizar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    return render(request, 'alumno/actualizar_alumno.html', {'alumno': alumno})

# 👉 Procesar el envío del formulario y actualizar en la base de datos
def realizar_actualizacion_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)

    if request.method == 'POST':
        alumno.nombre = request.POST.get('nombre')
        alumno.apellido = request.POST.get('apellido')
        alumno.correo = request.POST.get('correo')
        alumno.telefono = request.POST.get('telefono')
        alumno.direccion = request.POST.get('direccion')
        alumno.fecha_nacimiento = request.POST.get('fecha_nacimiento')

        # ✅ NO modificar fecha_registro, se deja igual
        alumno.save()

        return redirect('ver_alumno')

    # Si entra por GET, redirige al formulario de nuevo
    return render(request, 'alumno/actualizar_alumno.html', {'alumno': alumno})


def borrar_alumno(request, id):

    alumno = get_object_or_404(Alumno, id=id)

    if request.method == 'POST':

        alumno.delete()

        return redirect('ver_alumno')

    return render(request, 'alumno/borrar_alumno.html', {'alumno': alumno})
