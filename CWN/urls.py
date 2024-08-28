from django.contrib import admin
from django.urls import path, include
from django.urls import reverse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('blog.urls')),  # Your blog app's URLs
]

