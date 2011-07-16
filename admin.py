from django.contrib import admin
#from django import forms
#from tinymce.widgets import TinyMCE
from mptt.admin import MPTTModelAdmin
from djcode.blog.models import Category, Post, Tag

class CategoryAdmin(MPTTModelAdmin):
	fields = ('parent', 'name', 'description', 'category_order',)

#class PoastAdminForm(forms.ModelForm):
#	content = forms.CharField(widget=TinyMCE(attrs={'id':"action_short_description"}))    

class PostAdmin(admin.ModelAdmin):

	class Media:
		js = (
#			'/media/js/tiny_mce/tiny_mce.js',
			'/media/js/jquery/jquery.js',			
			'/media/js/tiny_mce/jquery.tinymce.js',			
			'/media/js/utils.js',
			'/media/js/textarea.js',
		)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
#admin.site.register(Tag)
