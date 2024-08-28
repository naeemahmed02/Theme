from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . views import *

urlpatterns = [

    path('', home, name='home'),
    path('blogs/<slug:slug>', singlePost, name='single-post'),
    path('articles', search, name='articles'),
    path('search', search, name='search'),
    path('privacy-policy', privacy_policy, name='privacy-policy'),
    path('terms-conditons', terms_conditions, name='terms-conditions'),
    path('django-projects', django_projects, name='django-projects'),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
