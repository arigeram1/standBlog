
from article_app.models import Article



def recent_articles(request):

    recent_articles = Article.objects.all().order_by('-created')[:3]

    return {'recent_articles':recent_articles}



