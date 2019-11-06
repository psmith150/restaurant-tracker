from django.db import models
from colorful.fields import RGBColorField
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator, DecimalValidator, ValidationError
from django.utils import timezone

#region Constants
MAX_PRICE_VALUE = 4
MIN_PRICE_VALUE = 1
MAX_RATING_VALUE = 10
MIN_RATING_VALUE = 1
#endregion

# Create your models here.
class Tag(models.Model):
    """
    Represents a Tag that describes a characteristic
    """
    name = models.CharField(max_length=50)
    color = RGBColorField(default='#FF0000')

    def __str__(self):
        return self.name

    def get_color_lightness(self):
        """
        Returns the lightness of the Tag's color, calculated using RGB values
        """
        color_string = self.color.__str__()
        red = int(color_string[1:3],16)
        green = int(color_string[3:5],16)
        blue = int(color_string[5:7],16)
        return (0.2126*red + 0.7152*green + 0.0722*blue)
    
    def is_light_color(self):
        """
        Returns True if the Tag's lightness is above the 'light color' threshold
        """
        return self.get_color_lightness() > 127
    
    def get_absolute_url(self):
        """
        Returns an absolute URL for editing an instance of a Tag
        """
        return reverse("restaurant_tracker:tag_edit", kwargs={"pk": self.pk})

class Restaurant(models.Model):
    """
    Represents a restaurant
    """
    name = models.CharField(max_length=200)
    rating = models.IntegerField('Rating', default=MIN_RATING_VALUE, validators=[MaxValueValidator(limit_value=MAX_RATING_VALUE), MinValueValidator(limit_value=MIN_RATING_VALUE)])
    price = models.IntegerField('Price', default=MIN_PRICE_VALUE, validators=[MaxValueValidator(limit_value=MAX_PRICE_VALUE), MinValueValidator(limit_value=MIN_PRICE_VALUE)])
    service = models.CharField(max_length=300, blank=True, default='')
    SLOW_SPEED = 1
    MEDIUM_SPEED = 2
    FAST_SPEED = 3
    SPEED_CHOICES = [
        (SLOW_SPEED, 'Slow'),
        (MEDIUM_SPEED, 'Medium'),
        (FAST_SPEED, 'Fast'),
    ]
    speed = models.IntegerField('Speed', choices=SPEED_CHOICES, default=SLOW_SPEED)
    comment = models.CharField(max_length=300, blank=True, default='')
    is_open = models.BooleanField(default=True)
    latitude = models.FloatField('Latitude', default=0.0)
    longitude = models.FloatField('Longitude', default=0.0)
    tags = models.ManyToManyField(Tag, verbose_name='Tags', blank=True)

    def save(self, *args, **kwargs):
        """
        Performs a full clean before saving the data
        """
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """
        Returns an absolute URL for editing an instance of a Restaurant
        """
        return reverse("restaurant_tracker:detail", kwargs={"pk": self.pk})
    
    def get_menu_items(self):
        """
        Returns a list of MenuItems associated with the Restaurant
        """
        try:
            menu_items = MenuItem.objects.filter(restaurant = self.pk)
        except MenuItem.DoesNotExist:
            menu_items = None
        return menu_items

class User(models.Model):
    """
    Represents a user
    """
    first_name = models.CharField('First Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    is_active = models.BooleanField('Is Active', default=True)

    def __str__(self):
        return self.fullName()

    def fullName(self):
        """
        Returns the formatted full name of the User
        """
        return self.first_name + ' ' + self.last_name

class CurrencyField(models.IntegerField):
    """
    A field to save dollars as pennies (int) in db, but act like a float
    """
    description = "A field to save dollars as pennies (int) in db, but act like a float"

    def get_db_prep_value(self, value, *args, **kwargs):
        """
        Converts the float value to an int for database storage
        """
        if value is None:
            return None
        return int(round(value * 100))

    def to_python(self, value):
        """
        Converts the database int value to a Python float value
        """
        if value is None or isinstance(value, float):
            return value
        try:
            return float(value) / 100
        except (TypeError, ValueError):
            raise ValidationError("This value must be an integer or a string that represents an integer.", code='invalid')

    def from_db_value(self, value, expression, connection, context):
        """
        Gets the value from the database
        """
        return self.to_python(value)

    def formfield(self, **kwargs):
        """
        Defines the field used in Django forms
        """
        from django.forms import FloatField
        defaults = {'form_class': FloatField}
        defaults.update(kwargs)
        return super(CurrencyField, self).formfield(**defaults)

class MenuItem(models.Model):
    """
    Represents an item ordered from the menu at a Restaurant
    """
    name = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField('Date', default=timezone.now)
    price = CurrencyField(verbose_name='Price', default=0)
    comment = models.CharField(max_length=300)
    rating = models.IntegerField('Rating', default=MIN_RATING_VALUE, validators=[MaxValueValidator(limit_value=MAX_RATING_VALUE), MinValueValidator(limit_value=MIN_RATING_VALUE)])



#Custom Fields

# class Location:
#     def __init__(self, latitude, longitude):
#         self.latitude = latitude
#         self.longitude = longitude

# class LocationField(forms.MultiValueField):
#     def __init__(self, *args, **kwargs):
#         fields = (
#             FloatField(max_value=90, min_value=-90), 
#             FloatField((max_value=90, min_value=-90)
#         )
#         super().__init__(*args, **kwargs)


#     def compress(self, data_list):
#         latitude, longitude = data_list
#         return Location(latitude, longitude)