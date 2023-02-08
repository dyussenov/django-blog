from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    return HttpResponse("Index page of blog application")


def about(request):
    return HttpResponse("About blog application")


def categories(request, category):
    return HttpResponse(f"Посты с категорией {category}")


def contact(request):
    return redirect("/about")