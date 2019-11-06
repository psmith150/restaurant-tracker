from django.test import TestCase
from django.urls import reverse

from .models import Restaurant, User, Tag, MenuItem

# Create your tests here.
class TagModelTests(TestCase):
    def test_tag_is_light(self):
        '''
        is_light_color() returns True for white
        '''
        light_tag = Tag(color='#FFFFFF')
        self.assertIs(light_tag.is_light_color(), True)
    def test_tag_is_dark(self):
        '''
        is_light_color() returns False for black
        '''
        light_tag = Tag(color='#000000')
        self.assertIs(light_tag.is_light_color(), False)

class RestaurantIndexViewTests(TestCase):
    def test_no_restaurants(self):
        '''
        If no restaurants exist, an appropriate message is displayed.
        '''
        response = self.client.get(reverse('restaurant_tracker:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No restaurants are available.")
        self.assertQuerysetEqual(response.context['restaurant_list'], [])