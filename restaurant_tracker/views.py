from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.forms import ModelForm
from .models import Restaurant, Tag
from .forms import RestaurantForm, TagForm

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'restaurant_tracker/index.html'
    context_object_name = 'restaurant_list'

    def get_queryset(self):
        return Restaurant.objects.order_by('name')

class RestaurantDetailView(generic.DetailView):
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
    model = Restaurant
    form_class = RestaurantForm
    template_name = "restaurant_tracker/restaurant_edit.html"

class RestaurantDeleteView(generic.edit.DeleteView):
    model = Restaurant
    success_url = reverse_lazy('restaurant_tracker:index')


def create_restaurant(request):
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