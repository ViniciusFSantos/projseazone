from .views import AnunciosListView, AnunciosDetailView
from django.urls import path

urlpatterns = [
    path('', AnunciosListView.as_view()),
    path('<int:pk>', AnunciosDetailView.as_view()),
]