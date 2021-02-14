from django.urls import path, re_path
from .views import (
    PostListView,
    PostDetailView,
    HowToListView,
    HowToDetailView,
    LinuxListView,
    LinuxDetailView
)


urlpatterns = [
    path('linux/<slug:slug>/', LinuxDetailView.as_view(), name='linux_detail'),
    path('linux/', LinuxListView.as_view(), name='linux_list'),
    path('howto/<slug:slug>/', HowToDetailView.as_view(), name='howto_detail'),
    path('howto/', HowToListView.as_view(), name='howto_list'),
    path('<slug:slug>/', PostDetailView.as_view(), name='blog_detail'),
    path('', PostListView.as_view(), name='blog_list'),
    # re_path(r'^(?P<page>\d+)/$', PostListView.as_view(), name='blog_list'),
]
