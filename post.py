# Create your views here.
from django.shortcuts import render_to_response

def view(request):
    """ show view post page """
    return render_to_response('blog/post.djhtml')