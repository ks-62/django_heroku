from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostCreateForm

# Create your views here.
def posts(request):
    # return render(request, 'blog/posts.html', {})
    # posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')
    # return render(request, 'blog/posts.html', {'posts':posts})
    posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')
    return render(request, 'blog/posts.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_at = timezone.now()
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostCreateForm()
    return render(request, 'blog/post_create.html', {'form': form})
