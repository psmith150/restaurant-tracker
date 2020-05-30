from django.forms import Form, ModelForm, inlineformset_factory
from django import forms
from .models import Restaurant, Tag, MenuItem
from .widgets import StarRatingWidget, PriceRatingWidget
from .models import MAX_PRICE_VALUE, MAX_RATING_VALUE

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'rating', 'price', 'service', 'speed', 'comment', 'is_open', 'tags']
        widgets = {
            'rating' : StarRatingWidget(stars=MAX_RATING_VALUE, halfStars=True, attrs={'id':'id_star-rating-rating'}),
            'price' : PriceRatingWidget(prices=MAX_PRICE_VALUE, attrs={'id':'id_price-rating-price'}),
            'service' : forms.Textarea(attrs={'id':'id_service'}),
            'comment' : forms.Textarea(attrs={'id':'id_comment'}),
            'is_open' : forms.Select(attrs={'id':'id_is_open'}, choices=((False, 'Closed'), (True, 'Open'))),
        }
        labels = {
            'speed': ('Service Speed'),
            'is_open': ('Open/Closed'),
        }

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'color']

class MenuItemForm(ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'user', 'date', 'price','rating', 'comment']

MenuItemsInlineFormSet = inlineformset_factory(Restaurant, MenuItem, form=MenuItemForm, extra=0)