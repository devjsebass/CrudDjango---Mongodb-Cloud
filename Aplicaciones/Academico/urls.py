from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('editarCurso/<codigo>', views.editarCurso),
    path('actualizarCurso/', views.actualizarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso)
]