from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.forms import ModelForm, inlineformset_factory
from django.db import transaction
from .models import Restaurant, Tag, MenuItem, User
from .forms import RestaurantForm, TagForm, MenuItemForm, MenuItemsInlineFormSet

# Create your views here.
class IndexView(generic.ListView):
    """
    Displays a list of all Restaurants
    """
    template_name = 'restaurant_tracker/index.html'
    context_object_name = 'restaurant_list'

    def get_queryset(self):
        return Restaurant.objects.order_by('name')

class RestaurantDetailView(generic.DetailView):
    """
    Displays a detail view of a Restaurant
    """
    model = Restaurant
    template_name = 'restaurant_tracker/restaurant_detail.html'
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # Redirect to index page
            return redirect('restaurant_tracker:index')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

class RestaurantEditView(generic.edit.UpdateView):
    """
    Displays a form for editing fields of a Restaurant
    """
    model = Restaurant
    form_class = RestaurantForm
    template_name = "restaurant_tracker/restaurant_edit.html"

    def get_context_data(self, **kwargs):
        data = super(RestaurantEditView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['menu_items'] = MenuItemsInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data['menu_items'] = MenuItemsInlineFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        menu_items = context['menu_items']
        with transaction.atomic():
            self.object = form.save()

            if menu_items.is_valid():
                menu_items.instance = self.object
                menu_items.save()
            else:
                pass
        return super(RestaurantEditView, self).form_valid(form)

class RestaurantDeleteView(generic.edit.DeleteView):
    """
    Displays a confirmation for deleting a Restaurant"""
    model = Restaurant
    success_url = reverse_lazy('restaurant_tracker:index')

def create_restaurant(request):
    """
    Creates a new restaurant
    """
    restaurant = Restaurant()
    restaurant.save()
    return HttpResponseRedirect(reverse('restaurant_tracker:restaurant_edit', args=(restaurant.id,)))

class TagIndexView(generic.ListView):
    template_name = 'restaurant_tracker/tags.html'
    context_object_name = 'tag_list'

    def get_queryset(self):
        return Tag.objects.order_by('id')

class TagEditView(generic.edit.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "restaurant_tracker/tag_edit.html"
    success_url = reverse_lazy('restaurant_tracker:tag_index')
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # Redirect to index page
            return redirect('restaurant_tracker:tag_index')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

class TagDeleteView(generic.edit.DeleteView):
    model = Tag
    success_url = reverse_lazy('restaurant_tracker:tag_index')

def create_tag(request):
    tag = Tag()
    tag.save()
    return HttpResponseRedirect(reverse('restaurant_tracker:tag_edit', args=(tag.id,)))

def create_menu_item(request, pk):
    menu_item = MenuItem()
    menu_item.restaurant = get_object_or_404(Restaurant, id=pk)
    first_user = User.objects.first()
    if (first_user is None):
        pass
    else:
        menu_item.user = User.objects.first()
    menu_item.save()
    return HttpResponseRedirect(reverse('restaurant_tracker:restaurant_edit', args=(pk,)))