from django.db import models
from colorful.fields import RGBColorField
from django.urls import reverse

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)
    color = RGBColorField(default='#FF0000')

    def __str__(self):
      return self.name
    
    def get_color_lightness(self):
      color_string = self.color.__str__()
      red = int(color_string[1:3],16)
      green = int(color_string[3:5],16)
      blue = int(color_string[5:7],16)
      return (0.2126*red + 0.7152*green + 0.0722*blue)
    
    def get_absolute_url(self):
        return reverse("restaurant_tracker:tag_edit", kwargs={"pk": self.pk})

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    rating = models.IntegerField('Rating', default=1)
    price = models.IntegerField('Price', default=1)
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
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("restaurant_tracker:detail", kwargs={"pk": self.pk})
    

class User(models.Model):
    first_name = models.CharField('First Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    is_active = models.BooleanField('Is Active', default=True)

    def __str__(self):
        return self.fullName()

    def fullName(self):
        return self.first_name + ' ' + self.last_name

class CurrencyField(models.IntegerField):
  description = "A field to save dollars as pennies (int) in db, but act like a float"

  def get_db_prep_value(self, value, *args, **kwargs):
    if value is None:
      return None
    return int(round(value * 100))

  def to_python(self, value):
    if value is None or isinstance(value, float):
      return value
    try:
      return float(value) / 100
    except (TypeError, ValueError):
      raise ValidationError("This value must be an integer or a string that represents an integer.")

  def from_db_value(self, value, expression, connection, context):
    return self.to_python(value)

  def formfield(self, **kwargs):
    from django.forms import FloatField
    defaults = {'form_class': FloatField}
    defaults.update(kwargs)
    return super(CurrencyField, self).formfield(**defaults)


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField('Date')
    price = CurrencyField(verbose_name='Price')
    comment = models.CharField(max_length=300)
    rating = models.IntegerField()



#Custom Fields

# class Location:
#     def __init__(self, latitude, longitude):
#         self.latitude = latitude
#         self.longitude = longitude

# class LocationField(models.MultiValueField):
#     def __init__(self, *args, **kwargs):
#         fields = (
#             FloatField(max_value=90, min_value=-90), 
#             FloatField((max_value=90, min_value=-90)
#         )
#         super().__init__(*args, **kwargs)


#     def compress(self, data_list):
#         latitude, longitude = data_list
#         return Location(latitude, longitude)