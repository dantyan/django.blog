from django.contrib import admin
from django.db import models
from mptt.models import MPTTModel
#import mptt

STATUS_CHOICES = (
    ('a', 'active'),
    ('d', 'deleted'),
)

# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child')
    description = models.TextField(blank=True,help_text="Optional")
    category_order = models.PositiveSmallIntegerField(blank=True, help_text="Optional", default=0)
    
#    class Meta:
#        ordering = ['id',]
    
#    class MPTTMeta:
#        level_attr = 'mptt_level'
#        order_insertion_by=['name']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/blog/category-%i/' % self.id

#mptt.register(Category,)
# ----------------------------------------------------------------------------------------------------------------------

class Post(models.Model):
	category = models.ManyToManyField(Category)
	name = models.CharField(max_length=200)
	text = models.TextField()
	summary = models.TextField()
	date_add = models.DateTimeField(auto_now_add=True)
	date_edit = models.DateTimeField(auto_now=True)
	date_show = models.DateTimeField(blank=True)
	status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='a', db_index = True)
	
	def __unicode__(self):
		return self.name
	
	def get_absolute_url(self):
		return '/blog/post-%i/' % self.id

# ----------------------------------------------------------------------------------------------------------------------

class PostMeta(models.Model):
	post = models.ForeignKey(Post)
	meta_key = models.CharField(max_length=250)
	meta_value = models.TextField()

# ----------------------------------------------------------------------------------------------------------------------

class Tag(models.Model):
	tag = models.CharField(max_length=30)
	post = models.ManyToManyField(Post)
	
	def get_absolute_url(self):
		return '/blog/tags/%s' % self.tag
