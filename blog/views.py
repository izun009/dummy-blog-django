from .models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q


# Create your views here.
class LinuxDetailView(DetailView):
    model = Post
    template_name = "blog/linux_detail.html"

class LinuxListView(ListView):
    model = Post
    template_name = "blog/linux_list.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(LinuxListView, self).get_context_data(**kwargs)
        
        # add extra field                       
        home_page_title = "Selamat Datang Di Blogku"
        home_sub_page_title = "Aku Sangat Menyukai Django Seperti Aku Menyukaimu..!"
        context["home_page_title"] = home_page_title
        context["home_sub_page_title"] = home_sub_page_title
        return context
    
    def get_queryset(self):
        
        qs = super().get_queryset()
        
        return qs.filter(
            Q(title__contains="Linux"),
            status = 1
        ).order_by('-created_on')

class HowToDetailView(DetailView):
    model = Post
    template_name = "blog/howto_detail.html"

class HowToListView(ListView):
    model = Post
    template_name = "blog/howto_list.html"
    #queryset = model.objects.filter(status=1).order_by('-created_on')
    paginate_by = 12                

    def get_context_data(self, *args, **kwargs):   

        context = super(HowToListView, self).get_context_data(*args, **kwargs) 
        
        # add extra field                       
        home_page_title = "Selamat Datang Di Blogku"
        home_sub_page_title = "Aku Sangat Menyukai Django Seperti Aku Menyukaimu..!"
        context["home_page_title"] = home_page_title
        context["home_sub_page_title"] = home_sub_page_title

        return context
    
    def get_queryset(self):
        
        qs = super().get_queryset()
        
        return qs.filter(
            Q(title__startswith="Bagaimana") | 
            Q(title__startswith="Cara") |
            Q(title__startswith="Bagaimana Cara"),
            status = 1
        ).order_by('-created_on')
    
    

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/blog_detail.html"
    context_object_name = 'post_list'

class PostListView(ListView):
    model = Post
    template_name = "blog/blog_list.html"
    paginate_by = 12
    context_object_name = 'post_list'
    
    #bisa mengganti object name di tag
    #context_object_name = 'blog_post'
    

    def get_context_data(self, *args, **kwargs):    

        context = super(PostListView, self).get_context_data(*args, **kwargs) 
        
        # add extra field                       
        home_page_title = "Selamat Datang Di Blogku"
        home_sub_page_title = "Aku Sangat Menyukai Django Seperti Aku Menyukaimu..!"

        context["home_page_title"] = home_page_title
        context["home_sub_page_title"] = home_sub_page_title

        return context

    def get_queryset(self):
        
        qs = super().get_queryset()
        
        return qs.filter(
            #status models
            status = 1
        ).order_by('-created_on') #hanya published dan diurut berdasarkan tgl buat
