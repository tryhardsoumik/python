

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('Aboutus', views.Aboutus, name='Aboutus'),

]