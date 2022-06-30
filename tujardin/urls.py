from django.urls import path
from .views import index, empresa, api, login, products, register, api_crear, api_modificar, api_borrar, api_cli, api_cli_crear, api_cli_modificar, api_cli_borrar


urlpatterns= [
path('', index, name="index"),
path('empresa/', empresa, name="empresa"),
path ('api/', api, name="api"),
path('login/', login, name="login"),
path('products/', products, name="products"),
path('register/', register, name="register"),
path ('api_crear/', api_crear, name="api_crear"),
path ('api_modificar/<id>', api_modificar, name="api_modificar"),
path ('api_borrar/<id>', api_borrar, name="api_borrar"),
path ('api_cli/', api_cli, name="api_cli"),
path ('api_cli_crear/', api_cli_crear, name="api_cli_crear"),
path ('api_cli_modificar/<id>', api_cli_modificar, name="api_cli_modificar"),
path ('api_cli_borrar/<id>', api_cli_borrar, name="api_cli_borrar"),
]

