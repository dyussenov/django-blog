from django.contrib import admin
from django.urls import include, path
from blog_app.views import page404
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('a/', include('blog_app.urls')),
    path('a/', include('django.contrib.auth.urls')),
]

handler404 = page404