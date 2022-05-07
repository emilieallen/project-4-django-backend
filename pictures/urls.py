from django.urls import path
from pictures.views import PictureDetailView, PictureListView


urlpatterns = [
    path("", PictureListView.as_view()),
    path("<int:pk>", PictureDetailView.as_view())
]