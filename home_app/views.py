from django.shortcuts import render

from article_app.models import Article

from account_app.models import Profile

def home(request):

    articles = Article.objects.all()

    # mylist = list(articles)
    #
    # recent_articles = reversed(mylist[-3:])

    recent_articles = Article.objects.all().order_by('-created')[:3]

    return render(request, 'home_app/home.html', context={'articles':articles , 'recent':recent_articles})




