from django.contrib import admin
from django import forms

from .models import Tutorial
    

# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
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

admin.site.register(Tutorial, TutorialAdmin)