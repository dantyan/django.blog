
# Create your views here.
from django.shortcuts import render_to_response
from djcode.blog.models import Post, Category

def welcome(request):
    """ show blog index page """
    import logging

    data = {}
    data['posts'] = Post.objects.all()
    data['categories'] = Category.objects.all()

    logging.debug(data) 

    return render_to_response('blog/welcome.djhtml', data)

def category(request, id):
    '''
        category page
    '''
    import logging
    
    data = {}
    data['category'] = Category.objects.get(id=id)
    data['posts'] = Post.objects.filter(category=id)
    
    logging.debug(data)
    
    return render_to_response('blog/category.djhtml', data)