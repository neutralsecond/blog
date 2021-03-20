from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Favorites
from .forms import PostForm

# Create your views here.
def post_list_all(request):
    posts = Post.objects.all().order_by('date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    is_mypost = (request.user == post.author)
    return render(request, 'blog/post_detail.html', {'post': post, 'is_mypost':is_mypost})

def post_list_blogger(request, pk):
    author = get_object_or_404(User, pk=pk)
    posts = Post.objects.filter(author=author).order_by('date')
    show_fav_icon = is_fav = False
    if request.user.is_authenticated and author != request.user:
        show_fav_icon = True
        is_fav = Favorites.objects.filter(blogger=request.user, favorite=author).exists()
    return render(request, 'blog/post_list.html', \
    {'posts': posts, 'author': author, 'is_fav': is_fav, 'show_fav_icon': show_fav_icon})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form, 'is_new': True})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list_blogger', pk=request.user.pk)

@login_required
def add_favorite_blogger(request, pk):
    author = get_object_or_404(User, pk=pk)
    fav = Favorites(blogger=request.user, favorite=author)
    fav.save()
    return redirect('post_list_blogger', pk=pk)

@login_required
def del_favorite_blogger(request, pk):
    fav = get_object_or_404(Favorites, blogger=request.user.pk, favorite=pk)
    fav.delete()
    return redirect('post_list_blogger', pk=pk)