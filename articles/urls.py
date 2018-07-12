from django.urls import path
from.import views

#Give urls a namespace to avoid namespace conflict
app_name = 'articles'
#Setup urls for the articles app
urlpatterns = [
    path('', views.article_list, name='list'),
    path('create/', views.article_create, name='create'),
    path('<slug>', views.article_detail, name='detail'),
]
