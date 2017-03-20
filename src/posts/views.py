from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def post_create(request):
    return HttpResponse("<h1>Create!</h2>")

def post_detail(request): # retrieve
    return HttpResponse("<h1>Detail!</h2>")

def post_list(request): # list itmes
    return HttpResponse("<h1>List!</h2>")

def post_update(request):
    return HttpResponse("<h1>Update!</h2>")

def post_delete(request):
    return HttpResponse("<h1>Delete!</h2>")

