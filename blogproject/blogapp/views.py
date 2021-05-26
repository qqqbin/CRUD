from .forms import PostForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.

def main(request):
    return render(request, 'blogapp/main.html')

def write(request):
    return render(request, 'blogapp/write.html')

def create(request):
    if request.method == 'POST' :
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('read')
    else:
        form = PostForm
        return render(request, 'blogapp/write.html', {'form':form})


def read(request):
    posts = Post.objects
    return render(request, 'blogapp/read.html', {'posts': posts})

def detail(request, id):
    post = get_object_or_404(Post, id = id)
    return render(request, 'blogapp/detail.html', {'post':post})

def edit(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('read')
    
    else :
        form = PostForm(instance=post)
        return render(request, 'blogapp/edit.html', {'form':form})

def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('read')
    

