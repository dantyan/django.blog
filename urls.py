from django.conf.urls.defaults import *


#(?P<year>\d{4})
urlpatterns = patterns('djcode.blog',
    (r'^$', 'views.welcome'),
    (r'^category-(?P<id>\d+)/$', 'views.category',),
)
