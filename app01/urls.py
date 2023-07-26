from django.urls import path
from . import views

# As rotas da aplicação.

urlpatterns = [
    path('', views.index, name='index'),
]
