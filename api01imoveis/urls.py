from .views import ImoveisListView, ImoveisDetailView
from django.urls import path

urlpatterns = [
    path('', ImoveisListView.as_view()),
    path('<int:pk>', ImoveisDetailView.as_view()),
]