from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rating', views.rating, name='rating'),
    path('calc', views.calc, name='calc'),
    path('test', views.test, name='test'),
    path('result', views.result, name='result'),
]