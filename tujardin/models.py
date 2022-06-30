from django.db import models

# Create your models here.
class Tipo(models.Model):
    idTipo = models.IntegerField(primary_key=True, verbose_name='Id-tipo')
    nomTipo=models.CharField(max_length=50, verbose_name='Nom-tipo')

    def str(self): 
        return self.nomTipo

class Producto (models.Model): 
    idprod = models.CharField(primary_key=True, max_length=6, verbose_name='Id')
    imgpro =models.ImageField(upload_to="Producto",null=True)
    nomprod= models.CharField(max_length=20, verbose_name='Nombre')
    precio= models.IntegerField(verbose_name='Precio')
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, verbose_name='Tipo')

    def str(self):
        return self.nomprod

class cliente (models.Model):
    idcli= models.CharField(primary_key=True,max_length=20, verbose_name='ID-cliente')
    email= models.CharField(max_length=30,verbose_name='Gmail')
    nom= models.CharField(max_length=10, verbose_name='Nombre')

    def str(self):
        return self.nom

