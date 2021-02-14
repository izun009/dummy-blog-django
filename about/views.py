from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class AboutView(TemplateView):
    template_name = "about/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        
        home_page_title = "Selamat Datang Di Blogku"
        home_sub_page_title = "Tentang Gue..."

        context["home_page_title"] = home_page_title
        context["home_sub_page_title"] = home_sub_page_title
        return context
    
