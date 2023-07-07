from django.db import models

# Create your models here.
class Artista(models.Model):
    nombre = models.CharField(max_length=70)
    imagen = models.ImageField(upload_to="artistas",null=True)
    destacado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Tipo(models.Model):
    nombre_tipo = models.CharField(max_length=70)
    def __str__(self):
        return self.nombre_tipo
    
class Producto(models.Model):
    nombre_pro = models.CharField(max_length=70)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="productos",null=True)
    artista = models.ForeignKey(Artista, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    def __str__(self):
        return self.nombre_pro
    

   