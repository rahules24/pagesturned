from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="BlogHome"),
    path("blogpost/", views.blogpost, name="BlogPost"),
    path("poempage/<int:poemid>", views.poempage, name="Poem"),
]
