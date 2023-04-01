from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('questions_home', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']


class Question(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        'blog_app.CustomUser',
        on_delete=models.CASCADE
    )
    likes = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    body = models.TextField()
    is_closed = models.BooleanField(default=False)
    favourites = models.ManyToManyField(
        CustomUser,
        related_name='favourite',
        default=None,
        blank=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_question', kwargs={
            'question_slug': self.slug
            }
        )


class Answer(models.Model):
    author = models.ForeignKey(
        'blog_app.CustomUser',
        on_delete=models.CASCADE
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    likes = models.ManyToManyField(CustomUser, related_name='like', default=None, blank=True)
    likes_count = models.IntegerField(default=0)
    body = models.TextField(default="")
    is_true_answer = models.BooleanField(default=0)

    def __str__(self):
        return self.body

    def change_status(self):
        question = Question.objects.get(pk=self.question.pk)
        answer = Answer.objects.get(pk=self.pk)
        if question.is_closed and answer.is_true_answer:
            answer.is_true_answer = False
            answer.save()

            question.is_closed = False
            question.save()
        elif question.is_closed:
            Answer.objects.filter(question=question).update(is_true_answer=False)
            answer.is_true_answer = True
            answer.save()

            question.is_closed = True
            question.save()
        else:
            answer.is_true_answer = True
            answer.save()

            question.is_closed = True
            question.save()
