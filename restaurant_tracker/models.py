from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    rating = models.IntegerField('Rating')
    price = models.IntegerField('Price')
    service = models.CharField(max_length=300)
    SLOW_SPEED = 1
    MEDIUM_SPEED = 2
    FAST_SPEED = 3
    SPEED_CHOICES = [
        (SLOW_SPEED, 'Slow'),
        (MEDIUM_SPEED, 'Medium'),
        (FAST_SPEED, 'Fast'),
    ]
    speed = models.IntegerField('Speed', choices=SPEED_CHOICES, default=SLOW_SPEED)
    comment = models.CharField(max_length=300)
    isOpen = models.BooleanField(default=True)
    latitude = models.FloatField('Latitude')
    longitude = models.FloatField('Longitude')

    def __str__(self):
        return self.name

class User(models.Model):
    firstName = models.CharField('First Name', max_length=100)
    lastName = models.CharField('Last Name', max_length=100)
    isActive = models.BooleanField('Is Active', default=True)

    def __str__(self):
        return self.fullName()

    def fullName(self):
        return self.firstName + ' ' + self.lastName

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
      raise ValidationError("This value must be an integer or a string represents an integer.")

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
    date = models.DateTimeField('Date')
    price = CurrencyField(verbose_name='Price')
    comment = models.CharField(max_length=300)
    rating = models.IntegerField()

class Tag(models.Model):
    name = models.CharField(max_length=50)
    restaurants = models.ManyToManyField(Restaurant, verbose_name="Restaurants")

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