from django.shortcuts import render, redirect
from .models import Producto, cliente
from .forms import prodform, clientform

# Create your views here.
def index(request):
    return render(request, 'index.html')
def empresa(request):
    return render(request, 'empresa.html')
def login(request):
    return render(request, 'login.html')
def products(request):
    return render(request, 'products.html')
def register(request):
    return render(request, 'register.html')
def api(request):
    productos= Producto.objects.all()
    datos={
        'productos': productos
    }
    return render(request, 'api.html', datos) 
def api_crear(request):
    if request.method=='POST': 
        prodform = prodform(request.POST)
        if prodform.is_valid():
            prodform.save()
            return redirect('index')
    else:
        prodform= prodform()
    return render(request, 'api_crear.html', {'prodform': prodform})
def api_modificar(request, id): 
    producto = Producto.objects.get(idprod=id)
    datos = {
        'form': prodform(instance=producto)
    }
    if request.method=='POST':
        formulario = prodform(data = request.POST, instance=producto)
        if formulario.is_valid: 
            formulario.save()
            return redirect ('api')
    return render (request, 'api_modificar.html', datos )
def api_borrar(request, id):
    producto = Producto.objects.get(idprod=id)
    producto.delete()
    return redirect ('api')
def api_cli_crear(request):
    if request.method=='POST': 
        clientform = clientform(request.POST)
        if clientform.is_valid():
            clientform.save()
            return redirect('index')
    else:
        clientform= clientform()
    return render(request, 'api_cli_crear.html', {'clientform': clientform})
def api_cli_modificar(request, id): 
    cliente = cliente.objects.get(idcli=id)
    datos = {
        'form': clientform(instance=cliente)
    }
    if request.method=='POST':
        formulario = clientform(data = request.POST, instance=cliente)
        if formulario.is_valid: 
            formulario.save()
            return redirect ('api_cli')
    return render (request, 'api_cli_modificar.html', datos )
def api_cli_borrar(request, id):
    cliente = cliente.objects.get(idcli=id)
    cliente.delete()
    return redirect ('api_cli')
def api_cli(request):
    clientes= cliente.objects.all()
    datos={
        'clientes': clientes
    }
    return render(request, 'api_cli.html', datos) 
