from django.shortcuts import render
from djnago.views.generic import ListView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'

def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/post_list.html',
        {
            'posts': posts,
        }
    )
# Create your views here.
