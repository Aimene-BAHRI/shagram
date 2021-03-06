# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.forms import modelformset_factory
from django.template import RequestContext
# Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from articles.models import Article, Categorie, Images
from events.models import Event

from .forms import PostForm, ImageForm
# Display all categories and all posts
def index(request):
    posts = Article.objects.all().order_by('-posted')[:5]
    categories = Categorie.objects.all().order_by('-id')
    images = Images.objects.all().order_by('-id')
    events = Event.objects.all().order_by('-id')
    today = timezone.now().date()
    paginator = Paginator(posts, 2) # Show 2 contacts per page
    page_request_variable = 'page'
    page = request.GET.get(page_request_variable)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
    'categories': categories,
    'posts' : posts,
    'images' : images,
    'events' : events,
    'today' : today,
    'paginator': queryset,
    'page_request_variable' : page_request_variable
    }
    return render(request, 'index.html', context)

# Create Post
def post_create(request):
    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=1)
    if request.method == 'POST':
        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Images.objects.none())
        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()
            for form in formset.cleaned_data:
                image = form['image']
                photo = Images(post=post_form, image=image)
                photo.save()
            messages.success(request,
                             "Yeeew,check it out on the home page!")
            return HttpResponseRedirect("/blog")
        else:
            print postForm.errors, formset.errors
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    context_instance=RequestContext(request)
    return render(request, 'post_form.html',
                  {
                      'postForm': postForm, 
                      'formset': formset,
                      'context_instance' : context_instance
                      })

# Display the post
def post_detail(request, id):
    article = get_object_or_404(Article, pk=id)
    events = Event.objects.all().order_by('-id')
    today = timezone.now().date()
    context ={
        'article' : article,
        'events' : events,
        'today' : today
    }
    return render(request, 'detail.html', context)
# Display the first 2 posts in a specefic category

# Create Post
def post_update(request, id):
    return HttpResponse("<h1>Update POST "+id+" </h1>")

# Create Post
def post_delete(request, id):
    return HttpResponse("<h1>Delete POST "+id+" </h1>")

