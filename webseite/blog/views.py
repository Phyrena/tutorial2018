from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import BlogPost
from .forms import PostForm
from django.views.decorators.http import require_POST

def index(request):
    return render(request, 'blog/base.html')


def timeline_view(request, username):
    post_form = PostForm()
    user = get_object_or_404(User, username=username)
    posts = BlogPost.objects.filter(user=user).order_by('-created_at')
    return render(request, 'blog/timeline.html', {'posts': posts, 'post_form': post_form, 'user': user})


@login_required
@require_POST
def post_view(request):
    post_form = PostForm(request.POST)
    if post_form.is_valid():
        post = post_form.save(commit=False)
        post.user = request.user
        post.save()
    return HttpResponseRedirect(reverse('blog:timeline', kwargs={'username': request.user.username}))



















