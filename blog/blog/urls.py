from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path
from blog_app.views import page404
from blog_app.forms import UserLoginForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_app.urls')),
    path(
        'login/',
        views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=UserLoginForm,
            ),
        name='login',
         ),
    path('', include('django.contrib.auth.urls')),
]

handler404 = page404