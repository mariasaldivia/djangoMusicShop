from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('artistas', views.artistas, name='artista'),
    path('registrate',views.signUp, name="registro"),
    path('cuenta',views.signIn, name="login"),
    path('visitanos',views.ub, name="ubicacion"),
    path('productos',views.producto, name='producto'),

    path('agregar_producto',views.agregar_producto, name='agregar-producto'),
    path('listar_producto',views.listar_producto, name='listar-producto'),
    path('modificar_producto/<id>',views.modificar_producto, name='modificar-producto'),
    path('eliminar_producto/<id>',views.eliminar_producto,name='eliminar-producto')
]