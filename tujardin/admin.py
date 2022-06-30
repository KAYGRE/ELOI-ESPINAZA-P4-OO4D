from django.contrib import admin
from .models import Tipo, Producto, cliente
# Register your models here.

admin.site.register(Tipo)
admin.site.register(Producto)
admin.site.register(cliente)


