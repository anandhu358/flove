from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('story/', views.story, name='story'),
    path('gallery/', views.gallery, name='gallery'),
    path('reasons/', views.reasons, name='reasons'),
    path('secret/', views.secret, name='secret'),
    path('first-chat/', views.first_chat, name='first_chat'),
path('first-call/', views.first_call, name='first_call'),
path('first-date/', views.first_date, name='first_date'),
path('favorite-memory/', views.favorite_memory, name='favorite_memory'),
path('counter/', views.counter, name='counter'),
path('lock/', views.lock, name='lock'),
]