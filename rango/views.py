from django.shortcuts import render
from rango.models import Category
from rango.models import Page
from django.http import HttpResponse


# Create your views here.

"""def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!', 'categories': category_list}
    context_dict['pages'] = page_list
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage': 'Hello World!!!'}
    return render(request, 'rango/about.html', context=context_dict)


def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}

    try:
        # The .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)

        # The filter() will return a list of page objects or an empty list.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)"""

def index(request):
    return HttpResponse("Rango says hey there partner!\n <a href='/rango/about/'>About</a>")


def about(request):
    return HttpResponse("Rango says here is the about page.\n <a href='/rango/'>Index</a>")


