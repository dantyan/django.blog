
# Create your views here.
from django.shortcuts import render_to_response
from djcode.blog.models import Post, Category

def welcome(request):
    """
        show blog index page
    """
    
#    import logging   

    data = {}
    data['categories'] = Category.objects.all()
    data['posts'] = Post.objects.all()
    

#    logging.debug(data) 

    return render_to_response('blog/welcome.djhtml', data)

def category(request, id):    
    '''
        category page
    '''
#    import logging
    
    data = {}
    data['categories'] = Category.objects.all()
    data['category'] = Category.objects.get(id=id)
    data['posts'] = Post.objects.filter(category=id)
    
#    logging.debug(data)
    
    return render_to_response('blog/category.djhtml', data)


def post(request, id):
    '''
        post page
    '''
#    import logging
    
    data = {}
    data['categories'] = Category.objects.all()    
    data['post'] = Post.objects.get(id=id)
        
#    logging.debug(data)
    
    return render_to_response('blog/post.djhtml', data)
   
def upload_post_image(request):
	'''
		upload image
	'''
	