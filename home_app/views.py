from django.shortcuts import render

from article_app.models import Article


def home(request):

    articles = Article.objects.all()

    return render(request,'home_app/index.html' , context={'articles':articles})




