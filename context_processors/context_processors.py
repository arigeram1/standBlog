
from article_app.models import Article

from article_app.models import Category


def recent_articles(request):

    recent_articles = Article.objects.all().order_by('-created')[:3]

    categories = Category.objects.all()

    return {'recent_articles':recent_articles,'categories':categories}



