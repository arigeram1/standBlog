from django.urls import path

from . import views

app_name = 'article_app'

urlpatterns = [

    path('detail/<int:article_id>',views.articleDetailView , name='detail')

]