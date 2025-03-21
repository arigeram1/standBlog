from django.urls import path

from . import views

app_name = 'article_app'

urlpatterns = [

    path('detail/<slug:slug>',views.articleDetailView , name='detail'),
    path('list',views.articleListView, name='article_list'),

]

