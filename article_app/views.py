from django.shortcuts import render

from .models import Article



def articleDetailView(request,article_id):

    article = Article.objects.get(id=article_id)

    return render(request,'article_app/article_details.html', context={'article':article})
