from django.http import HttpResponse


def first(request):
    return HttpResponse("Hey! It's your first view!!")


def articles(req):
    return HttpResponse("Articles")


def article(req, article_number):
    return HttpResponse(f"Articles {article_number}")


def article_archieve(req, article_number):
    return HttpResponse(f"Articles {article_number}. Archieve")


def article_slug(req, article_number, slug_text):
    return HttpResponse(f"Articles {article_number}. {slug_text}")


def articles_archieve(req):
    return HttpResponse("Articles Archieve")


def users(req):
    return HttpResponse(f"Users")


def user(req, user_id):
    return HttpResponse(f"Users {user_id}")


def phone_number(req, num):
    return HttpResponse(f"Phone: {num}")


def slug_url(req, slug_text):
    return HttpResponse(f"URL: {slug_text}")
