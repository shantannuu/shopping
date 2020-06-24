from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
from . import views

# Create your views here.
def index(request):
    myposts = Blogpost.objects.all()
    print(myposts)
    return render(request, 'blog/index.html', {'myposts': myposts})

def Post(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)


    return render(request, 'blog/Post.html', {'post':post})
