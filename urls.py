from django.conf.urls.defaults import *

urlpatterns = patterns('djcode.blog',
    (r'^$', 'views.welcome'),
)
