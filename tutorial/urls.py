from django.urls import path
from .views import (
    TutorialListView,
    TutorialDetailView
)


urlpatterns = [
    path('<slug:slug>/', TutorialDetailView.as_view(), name='detail'),
    path('', TutorialListView.as_view(), name='list'),
]

app_name = 'tutorial'