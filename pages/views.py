
from django.db.models import Prefetch
from django.views.generic import DetailView, ListView, TemplateView

from .models import Article, Category


class HomePageView(ListView):
    model = Article
    template_name = "home.html"
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.filter(
            status="published"
        ).select_related("category", "author")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        published_articles = Article.objects.filter(
            status="published"
        ).select_related("author")

        context["section_categories"] = (
            Category.objects.filter(
                slug__in=["world", "local", "sports", "weather", "business"]
            )
            .prefetch_related(
                Prefetch("articles", queryset=published_articles)
            )
        )

        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = "category_detail.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["articles"] = self.object.articles.filter(
            status="published"
        ).select_related("author")

        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = "article"

    def get_queryset(self):
        return Article.objects.filter(
            status="published"
        ).select_related("category", "author")


class AboutPageView(TemplateView):
    template_name = "about.html"


class ContactPageView(TemplateView):
    template_name = "contact.html"
