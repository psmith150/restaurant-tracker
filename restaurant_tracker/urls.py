from django.urls import path

from . import views

app_name = 'restaurant_tracker'
urlpatterns = [
    path('', views.index, name='index'),
]
