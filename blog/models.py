from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
STATUS = (
    (0, 'Draft'),
    (1, 'Published')
)

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    thumbnail = models.ImageField(upload_to = 'uploads/', default = 'uploads/my-avatar.png')
    content = RichTextField(
        blank=True, 
        null=True,
        extra_plugins=[
            'image2'
            ],
        )
    category = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    slug = models.SlugField(blank=True, editable=False)
    # slug = models.SlugField(max_length=255, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # buat slug dengan title
    def save(self):
        self.slug = slugify(self.title)
        super().save()
    
    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title
    

