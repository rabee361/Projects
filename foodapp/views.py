from django.shortcuts import render , redirect
from .models import *
from django.db.models import Q
import json
from django.views.generic import ListView
from django.contrib.postgres.search import SearchVector , SearchQuery, SearchRank

def index(request):
    search_queries = []
    tags = request.GET.get('tags') if request.GET.get('tags') != None else ''
    if tags:
        tags_list = json.loads(tags)
        search_queries = [item["value"] for item in tags_list]
        recipes = Recipe.objects.only('ingredient__ingredient_name__name')\
                        .prefetch_related('ingredient').\
                        filter(ingredient__ingredient_name__name__in=search_queries).distinct('id')
    else:
        recipes = Recipe.objects.all()


    context = {
        'recipes' : recipes
    }
    return render(request , 'index.html' , context)

 

def contact(request):
    if request.method =='POST':
        message = Messages.objects.get_or_create(
            writer=request.POST['name'],
            email = request.POST['email'],
            message=request.POST['message']
        )
        return redirect('contact')
    return render(request , 'contact.html')


# def blog(request):
#     blogs = Blog.objects.all()
#     context = {
#         'blogs' : blogs
#     }
#     return render(request,'blog.html' , context)



class ListBlogs(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'
    paginate_by = 3




def test(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ''
    recipes = Recipe.objects.filter(ingredient__ingredient_name__name__contains = q).distinct()

    context = {
        'recipes' : recipes
    }
    return render(request,'test.html' , context)


def single_blog(request, pk):
    blog = Blog.objects.get(id=pk)

    context = {
        'blog' : blog,

    }
    return render(request,'single-blog.html' , context)


def about(request):
    context = {
        
    }
    return render(request , 'about.html' , context)