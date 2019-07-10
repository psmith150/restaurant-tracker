from django.urls import path

from . import views

app_name = 'restaurant_tracker'
urlpatterns = [
    # ex: /restaurants/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /restaurants/1/
    path('<int:pk>/', views.RestaurantDetailView.as_view(), name='detail'),
    # ex: /restaurants/1/edit/
    path('<int:pk>/edit/', views.RestaurantEditView.as_view(), name='restaurant_edit'),
    # ex: /restaurants/create/
    path('create/', views.create_restaurant, name='restaurant_create'),
    path('<int:pk>/delete/', views.RestaurantDeleteView.as_view(), name='restaurant_delete'),
]
