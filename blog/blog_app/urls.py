from django.urls import path
from .views import SignUpView

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('about/', about, name='about'), 
    path('categories/<str:category>/', categories),
    path('contact/', contact),
    path('archive/<int:year>/', archive)
]