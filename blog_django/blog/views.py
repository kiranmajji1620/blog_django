from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("hello world")

from .models import Post
posts = [
    {
        'author' : 'Kiran',
        'title' : 'Title 1',
        'content' : 'Content 1',
        'date'  : 'august 9'
    },
    {
        'author' : 'Sai',
        'title' : 'Title 2',
        'content' : 'Content 2',
        'date'  : 'august 10'
    }
]
def home(request):
    # context = {
    #     'posts' : posts,
    #     'title' : 'Title 1'
    # }
    context = {
        'posts' : Post.objects.all(),
        'title' : 'Random title 98'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, "blog/about.html")