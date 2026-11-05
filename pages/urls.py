
from django.urls import path

from .views import (
    AboutPageView,
    ArticleDetailView,
    CategoryDetailView,
    ContactPageView,
    HomePageView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),

    path(
        "category/<slug:slug>/",
        CategoryDetailView.as_view(),
        name="category_detail",
    ),

    path(
        "article/<slug:slug>/",
        ArticleDetailView.as_view(),
        name="article_detail",
    ),
]
