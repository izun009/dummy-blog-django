from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'created_on',
        'updated_on',
    ]
    list_display = ('title', 'author', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']

    #automatic slug filled
    # prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
