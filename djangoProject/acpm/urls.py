from django.urls import path

from . import views


urlpatterns = [
    path("post/", views.PostListView.as_view()),
    path("post/<str:category>/<str:tag>", views.PostDetailView.as_view()),


]