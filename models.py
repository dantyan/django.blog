from django.contrib import admin
from django.db import models
from mptt.models import MPTTModel
#from local_models import RichTextFieldWithClass
#import mptt

STATUS_CHOICES = (
    ('active', 'active'),
    ('inactive', 'inactive'),
    ('draft', 'draft'),
    ('deleted', 'deleted'),
)
TYPE_CHOICES = (
	('standard', 'standard'),
	('note', 'note'),
	('link', 'link'),
	('image', 'image'),
	('gallery', 'gallery'),
	('status', 'status'),
	('quote', 'quote'),
)

# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child')
    description = models.TextField(blank=True,help_text="Optional")
    category_order = models.PositiveSmallIntegerField(blank=True, help_text="Optional", default=0)
    
    class Meta:
        ordering = ['lft',]
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/blog/category-%i/' % self.id

#mptt.register(Category,)
# ----------------------------------------------------------------------------------------------------------------------

class Post(models.Model):
	category = models.ManyToManyField(Category)
	title = models.CharField(max_length=200)
#	conent = RichTextFieldWithClass(css_class='mceEditor', plaintext_field='plaintext')
	content = models.TextField()
	date_add = models.DateTimeField(auto_now_add=True)
	date_edit = models.DateTimeField(auto_now=True)
	post_status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='active', db_index = True)
	post_type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='standard', db_index = True)
    
	class Meta:
		ordering = ['-id',]
    
	def __unicode__(self):
		return self.title
	
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
