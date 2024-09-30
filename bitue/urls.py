from django.urls import re_path as url

from django.urls import path
from bitue import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact' ),
    path('about/', views.about, name='about')
]
