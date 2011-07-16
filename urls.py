from django.conf.urls.defaults import *


#(?P<year>\d{4})
urlpatterns = patterns('djcode.blog',
    (r'^$', 'views.welcome'),
    (r'^category-(?P<id>\d+)/$', 'views.category',),
    (r'^post-(?P<id>\d+)/$', 'views.post',),
    (r'^ajax/upload_post_image/$', 'views.upload_post_image',),    
)
