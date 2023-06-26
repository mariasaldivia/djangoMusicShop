from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='index'),
    path('artista', views.artistas, name='artistas'),
    path('signup',views.signUp, name="registro"),
    path('signin',views.signIn, name="login"),
    path('ubicacion',views.ub, name="ubicacion"),
    path('productos',views.producto, name='productos')
]