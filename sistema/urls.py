from django.urls import path
from . import views

urlpatterns = [
    path('', views.sistema_info, name='sistema_info'),
]
