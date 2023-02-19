from django.urls import path
from .views import SignUpView
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('about/', about, name='about'),
    path('categories/', TemplateView.as_view(template_name='categories_list.html'), name='categories_list'),
    path('categories/<str:category>/', categories),
    path('contact/', contact),
    path('archive/<int:year>/', archive)
]