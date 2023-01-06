from .views import ReservasListView, ReservasDetailView
from django.urls import path

urlpatterns = [
    path('', ReservasListView.as_view()),
    path('<str:pk>', ReservasDetailView.as_view()),
]