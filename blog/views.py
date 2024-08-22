from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
posts = [
    {
        'author':'Fagbemi Oluwatobi',
        'title':'Introduction to Django',
        'content': 'Intro, basic and content of django',
        'date_created':'22nd august 2023'

    },
    {
        'author':'Fagbemi Oluwatobi',
        'title':'Introduction to python',
        'content': 'Intro, basic and content of python',
        'date_created':'24th august 2023'

    }
]

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'Aboutpage'})

def post_detail(request):
    return render(request, 'blog/post_detail.html', {'title': 'Post_detail'})