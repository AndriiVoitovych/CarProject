from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('', views.index, name='index'),
    url(r'^addCar/$', views.addCar, name='addCar'),
]  