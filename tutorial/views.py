from django.shortcuts import render
from .models import Tutorial
from django.views.generic import ListView, DetailView

# Create your views here.
class TutorialDetailView(DetailView):
    model = Tutorial
    context_object_name = 'tutorial_list' 
    template_name = "tutorial/tutorial_detail.html"

class TutorialListView(ListView):
    model = Tutorial
    paginate_by = 5
    context_object_name = 'tutorial_list'
    template_name = "tutorial/tutorial_list.html"

    def get_context_data(self, *args, **kwargs):    

        context = super(TutorialListView, self).get_context_data(*args, **kwargs) 
        
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
