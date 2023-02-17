from django.contrib import admin
from django.urls import include, path
from blog_app.views import page404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_app.urls')),
    path('', include('django.contrib.auth.urls')),
]

handler404 = page404