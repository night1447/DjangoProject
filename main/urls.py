
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='main-page'),
    path('abonements/', views.abonements, name='abonements'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('trainers/', views.trainers, name='trainers'),
    path('sertificates/', views.sertificates, name='sertificates'),
    path('contacts/', views.contacts, name='contacts'),
    path('forum/', views.forum, name='forum'),

]
