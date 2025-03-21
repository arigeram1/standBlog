from django.shortcuts import render

from .models import Article



def articleDetailView(request,slug):

    article = Article.objects.get(slug=slug)

    return render(request,'article_app/article_details.html', context={'article':article})


def articleListView(request):

    articles = Article.objects.all()

    return render(request,'article_app/article_list.html', context={'articles':articles})
