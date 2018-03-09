from django.shortcuts import render
from .models import BlogPost
from .forms import BlogPostForm

from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)


def post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blogs/post.html', context)


def add_post(request):
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))
    context = {'form': form}
    return render(request, 'blogs/add_post.html', context)


def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)

    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:post', args=[post_id]))
    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
