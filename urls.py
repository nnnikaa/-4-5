from .views import index, top_sellers, register
from django.urls import path

urlpatterns = [
    path('', index, name = 'main-page'),
    path('top-sellers', top_sellers, name = 'top-sellers'),
    path('register', register, name = 'register')
]