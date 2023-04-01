from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('categories/', TemplateView.as_view(template_name='categories_list.html'), name='categories_list'),
    path('q/<slug:question_slug>/', QuestionView.as_view(), name='show_question'),
    path('question/', login_required(AddQuestionView.as_view()), name='add_question'),
    path('questions/<slug:category_slug>/', QuestionsListView.as_view(), name='questions_home'),
    path('bookmarks/<int:question_id>/', favourite_add, name='favourite_add'),
    path('bookmarks/', favourite_list, name='bookmarks'),
    path('like/', like, name='like'),
    path('set-true-answer/<int:answer_id>', change_answer_status, name='set-true-answer'),
]