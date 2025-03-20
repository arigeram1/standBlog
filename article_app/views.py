from django.shortcuts import render

from .models import Article



def articleDetailView(request,slug):

    article = Article.objects.get(slug=slug)

    return render(request,'article_app/article_details.html', context={'article':article})
