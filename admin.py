from django.contrib import admin
from djcode.blog.models import Category, Post, Tag

class CategoryAdmin(admin.ModelAdmin):
    slug = admin.SlugField(core=True, prepopulate_from=('name',))
    
    fields = ('parent', 'name', 'description', 'category_order',)
    

#class PostAdmin(admin.ModelAdmin):
#    list_display = ('title', 'publisher', 'publication_date')
#    list_filter = ('publication_date',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post)
admin.site.register(Tag)
