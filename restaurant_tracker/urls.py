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
    path('tags/', views.TagIndexView.as_view(), name='tag_index'),
    path('tags/<int:pk>/edit/', views.TagEditView.as_view(), name='tag_edit'),
    path('tags/create/', views.create_tag, name='tag_create'),
    path('tags/<int:pk>/delete/', views.TagDeleteView.as_view(), name='tag_delete'),
    path('<int:pk>/menu_items/edit', views.edit_menu_item, name='menu_items_edit'),
    path('<int:pk>/menu_items/create/', views.create_menu_item, name='menu_item_create'),
]
