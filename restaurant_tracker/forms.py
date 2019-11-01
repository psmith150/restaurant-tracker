from django.forms import Form, ModelForm
from .models import Restaurant, Tag

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'rating', 'price', 'service', 'speed', 'comment', 'is_open', 'tags']

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'color']