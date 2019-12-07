from django.contrib import admin

from .models import Restaurant, User, MenuItem, Tag

# Register your models here
class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1
    verbose_name = 'Menu Item'
    verbose_name_plural = 'Menu Items'

class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'is_open', 'latitude', 'longitude']}),
        ('Ratings', {'fields': ['rating', 'price', 'speed', 'service']}),
        ('Comments', {'fields': ['comment']}),
        ('Tags', {'fields': ['tags']})
    ]
    filter_horizontal = ['tags']
    inlines = [MenuItemInline]
    list_display = ['name']
    list_filter = ['is_open']
    search_fields = ['name']

class TagAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'color']}),
    ]

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['first_name', 'last_name', 'is_active']})
    ]

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(User, UserAdmin)