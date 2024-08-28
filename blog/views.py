from django.shortcuts import render
from . models import Post
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    posts = Post.objects.all()[:5]
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def singlePost(request, slug):
    post = Post.objects.get(slug = slug)
    context = {'post': post}
    return render(request, 'blog/post.html', context)

def search(request):
    query = request.GET.get('q') if request.GET.get('q') is not None else ''

    articles = Post.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query)
    ).distinct()

    p = Paginator(articles, 10)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    context = {'page_obj': page_obj}
    return render(request, 'blog/articles.html', context)


def privacy_policy(request):
    return render(request, 'blog/maintanance.html')


def terms_conditions(request):
    return render(request, 'blog/maintanance.html')

def django_projects(request):
    return render(request, 'blog/maintanance.html')