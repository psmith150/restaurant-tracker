from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic

# Create your views here.
# class IndexView(generic.ListView):
#     template_name = 'restaurant_tracker/index.html'
#     context_object_name = 'restaurant_list'
def index(request):
    return HttpResponse("Hello, world. You're at the restaurant_tracker index.")
