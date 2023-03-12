from django.contrib import admin
from newspaper_blog.models import Post, Tag, Category, Contact, Comment
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Comment)