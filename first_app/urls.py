from django.urls import path
from . import views

urlpatterns = [
    path('456', views.index, name='index')
]