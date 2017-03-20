from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
# Create your views here.

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
    # if request.method == "POST":
    #     print(request.POST.get("title"))
    #     print(request.POST.get("content"))
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)

def post_detail(request, id=None): # retrieve
    instanace = get_object_or_404(Post, id=id)
    context = {
        "title": instanace.title,
        "instance": instanace,
    }
    return render(request, "post_detail.html", context)

def post_list(request): # list itmes
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, "index.html", context)

def post_update(request):
    return HttpResponse("<h1>Update!</h2>")

def post_delete(request):
    return HttpResponse("<h1>Delete!</h2>")

