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
    # ex: /restaurants/1/delete/
    path('<int:pk>/delete/', views.RestaurantDeleteView.as_view(), name='restaurant_delete'),
    # ex: /restaurants/tags/
    path('tags/', views.TagIndexView.as_view(), name='tag_index'),
    # ex: /restaurants/tags/1/edit/
    path('tags/<int:pk>/edit/', views.TagEditView.as_view(), name='tag_edit'),
    # ex: /restaurants/tags/create/
    path('tags/create/', views.create_tag, name='tag_create'),
    # ex: /restaurants/tags/1/delete/
    path('tags/<int:pk>/delete/', views.TagDeleteView.as_view(), name='tag_delete'),
    # ex: /restaurants/1/menu_items/create/
    path('<int:pk>/menu_items/create/', views.get_new_menu_item, name='menu_item_create'),
]
