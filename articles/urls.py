from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('category/', views.category, name='category'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
]
