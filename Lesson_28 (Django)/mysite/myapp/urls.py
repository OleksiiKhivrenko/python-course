from django.urls import re_path
from django.urls import path
from myapp.views import first, slug_url
from myapp.views import articles, article, articles_archieve, article_archieve, article_slug, users, user, phone_number

urlpatterns = [
    path('', first),
    path('articles/', articles),
    path('articles/archieve', articles_archieve),
    path('articles/<int:article_number>', article),
    path('articles/<int:article_number>/archieve', article_archieve),
    path('articles/<int:article_number>/<slug:slug_text>', article_slug),
    path('users', users),
    path('users/<int:user_id>', user),
    re_path(r'(?P<num>[0]{1}\d{2}\d{7})', phone_number),
    re_path(r'(?P<slug_text>\w{4}\-\w{4})', slug_url)
]

# засунуть в переменные
