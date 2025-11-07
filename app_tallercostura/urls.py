
from django.urls import path

from . import views



urlpatterns = [

    path('', views.inicio_tallercostura, name='inicio_tallercostura'),

    path('alumno/', views.ver_alumno, name='ver_alumno'),

    path('alumno/agregar/', views.agregar_alumno, name='agregar_alumno'),

    path('alumno/actualizar/<int:id>/', views.actualizar_alumno, name='actualizar_alumno'),

    path('alumno/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_alumno, name='realizar_actualizacion_alumno'),

    path('alumno/borrar/<int:id>/', views.borrar_alumno, name='borrar_alumno'),

]
