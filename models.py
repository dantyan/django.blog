from django.contrib import admin
from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200)
	parent = models.ForeignKey('self', blank=True, null=True, related_name='child')
	description = models.TextField(blank=True,help_text="Optional")
	category_order = models.IntegerField(blank=True,help_text="Optional",default=0)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return '/blog/category-%i' % self.id

# ----------------------------------------------------------------------------------------------------------------------

class Post(models.Model):
	category = models.ManyToManyField(Category)
	name = models.CharField(max_length=200)
	text = models.TextField()
	summary = models.TextField()
	date_add = models.DateTimeField(auto_now_add=True)
	date_edit = models.DateTimeField(auto_now=True)
	date_show = models.DateTimeField(blank=True)

# ----------------------------------------------------------------------------------------------------------------------

class PostMeta(models.Model):
	post = models.ForeignKey(Post)
	meta_key = models.CharField(max_length=250)
	meta_value = models.TextField()

# ----------------------------------------------------------------------------------------------------------------------

class Tag(models.Model):
	tag = models.CharField(max_length=30)
	post = models.ManyToManyField(Post)
