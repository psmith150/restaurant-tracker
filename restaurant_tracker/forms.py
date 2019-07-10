from django.forms import Form, ModelForm
from .models import Restaurant

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'tags']