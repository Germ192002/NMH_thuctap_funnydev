from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,  name="home"),
    path('about/', views.about, name="about"),
    path('category/', views.category, name="category"),
    path('latestNews/', views.latestNews, name="latestNews"),
    path('contact/', views.contact, name="contact"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('filter_category/<int:category_id>', views.filter_category, name="filter_category"),
    path('search_results/', views.search_results, name='search_results'),
    
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )