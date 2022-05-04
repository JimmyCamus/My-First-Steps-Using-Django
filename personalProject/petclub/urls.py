from django.urls import path

from . import views

urlpatterns = [
    path('', views.HelloWorld.as_view(), name='helloworld'),
    path('persons/', views.PersonAPIWiew.as_view()),
    path('pets/', views.PetAPIWiew.as_view()),
]
