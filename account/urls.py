from django.urls import path
from django.urls.conf import include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('login_user', views.login_user, name='login_user'),
   path('dashboard', views.dashboard, name='dashboard')
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
