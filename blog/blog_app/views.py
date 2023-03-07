from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.utils.text import slugify
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class AddQuestionView(CreateView):
    form_class = AddQuestionForm
    template_name = 'add_question.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.data['title'])
        return super(AddQuestionView, self).form_valid(form)


class QuestionsListView(ListView):
    model = Question
    template_name = 'questions_home.html'
    context_object_name = 'questions'
    paginate_by = 10

    def get_queryset(self):
        questions = Question.objects.all()
        if self.kwargs.get('category_slug'):
            return questions.filter(category__slug=self.kwargs['category_slug'])
        return questions


@login_required
def favourite_add(request, question_id):
    post = get_object_or_404(Question, id=question_id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class QuestionView(FormMixin, DetailView):
    model = Question
    template_name = 'question.html'
    slug_url_kwarg = 'question_slug'
    context_object_name = 'question'
    form_class = AddAnswerForm

    def get_context_data(self, *args, **kwargs):
        context = super(QuestionView, self).get_context_data(*args, **kwargs)
        context['answers'] = Answer.objects.filter(question_id=self.object)
        return context

    def get_success_url(self):
        return reverse_lazy('show_question', kwargs={'question_slug': self.object.slug})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.question = self.object
        print(form.data)
        form.save()
        return super(QuestionView, self).form_valid(form)


def index(request):
    return render(request, "home.html")


def page404(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
