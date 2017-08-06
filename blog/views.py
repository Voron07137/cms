from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import CommentForm


# Create your views here.

def list_of_post_by_category(request, category_slug):
    categories = Category.objects.all()
    post = Post.objects.filter(status='published')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        post = post.filter(category=category)
    template = 'category/list_of_post_by_category.html'
    context = {'categories': categories, 'post': post, 'category': category}
    return render(request, template, context)


def list_of_post(request):
    post = Post.objects.filter(status='published')
    categories = Category.objects.all()
    template = 'post/list_of_post.html'
    context = {'post': post, 'categories': categories}
    return render(request, template, context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    template = 'post/post_detail.html'
    categories = Category.objects.all()
    # category = get_object_or_404(Category, slug=slug)
    context = {'post': post, 'categories': categories}
    return render(request, template, context)


def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    categories = Category.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = CommentForm()
    template = 'post/add_comment.html'
    context = {'post': post, 'categories': categories, 'form': form}
    return render(request, template, context)


def twitter_reference(request):
    template = 'references/social_net/Twitter.html'
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, template, context)


def rss_reference(request):
    template = 'references/social_net/RSS.html'
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, template, context)


def archives_reference(request):
    template = 'references/archives.html'
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, template, context)


def contact_reference(request):
    template = 'references/contact.html'
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, template, context)


def about_reference(request):
    template = 'references/about.html'
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, template, context)



