from django.forms.widgets import Widget
from django.template import loader
from django.utils.safestring import mark_safe

DEFAULT_STARS = 5

class StarRatingWidget(Widget):
    template_name = 'restaurant_tracker/star_rating_widget.html'

    def __init__(self, attrs=None, stars=None, halfStars=False):
        super(StarRatingWidget, self).__init__(attrs)

        self.stars = stars if stars else DEFAULT_STARS
        if (halfStars):
            self.stars = self.stars * 2

    def get_context(self, name, value, attrs=None):
        context = super(StarRatingWidget, self).get_context(name, value, attrs)
        context['stars'] = range(1, self.stars+1, 1)
        return context