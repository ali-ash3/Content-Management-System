from django.shortcuts import get_object_or_404, render

from .models import Article, Category
# Create your views here.


def homepage(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "articles/homepage.html", context)

def article_detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    context = {"article":article}
    return render(request, "articles/article_detail.html", context)

def category(request):
    categories = Category.objects.all()
    context = {"categories":categories}
    return render(request, "articles/category.html", context)


def category_detail(request, category_id):
    category = Category.objects.get(pk=category_id)
    articles = category.article_set.all()
    context = {"category": category, "articles": articles}
    return render(request, "articles/category_detail.html", context)

