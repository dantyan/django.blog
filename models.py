from django.forms.widgets import SelectMultiple
from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField()
	parent = models.ForeignKey('self', blank=True, null=True, related_name='child')
	description = models.TextField(blank=True,help_text="Optional")

	class Admin:
		list_display = ('name', '_parents_repr')

	def __str__(self):
		p_list = self._recurse_for_parents(self)
		p_list.append(self.name)
		return self.get_separator().join(p_list)

	def get_absolute_url(self):
		if self.parent_id:
				return "/tag/%s/%s/" % (self.parent.slug, self.slug)
		else:
				return "/tag/%s/" % (self.slug)

	def _recurse_for_parents(self, cat_obj):
		p_list = []
		if cat_obj.parent_id:
				p = cat_obj.parent
				p_list.append(p.name)
				more = self._recurse_for_parents(p)
				p_list.extend(more)
		if cat_obj == self and p_list:
				p_list.reverse()
		return p_list

	def get_separator(self):
		return ' :: '

	def _parents_repr(self):
		p_list = self._recurse_for_parents(self)
		return self.get_separator().join(p_list)

	_parents_repr.short_description = "Tag parents"

	def save(self):
		p_list = self._recurse_for_parents(self)
		if self.name in p_list:
			raise validators.ValidationError("You must not save a category in itself!")
		super(Category, self).save()
    
    
class Post(models.Model):
    name = models.CharField(max_length=250)
    category = models.ManyToManyField(Category)
    slug = models.SlugField()
    text = models.TextField()
    summary = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    date_show = models.DateTimeField(blank=True)
    
    def __unicode__(self):
        return self.name



class PostMeta(models.Model):
    post_id = models.ForeignKey(Post)
    meta_key = models.CharField(max_length=250)
    meta_value = models.TextField()

class Tag(models.Model):
    tag = models.CharField(max_length=30)
    post = models.ManyToManyField(Post)
    


    
#class Enum( object ):
#    def __init__( self, **kwargs ):
#        self.attrs = kwargs
#        for key, value in kwargs.iteritems():
#            setattr( self, key, key )
#
#    def __iter__(self):
#        return self.attrs.iteritems()