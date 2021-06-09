from django.contrib import admin
from .models import  Post, Blogpostcomment
# Register your models here.

admin.site.register((Blogpostcomment))

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)
