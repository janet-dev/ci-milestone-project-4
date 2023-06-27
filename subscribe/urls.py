from . import views
from django.urls import path

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
]
