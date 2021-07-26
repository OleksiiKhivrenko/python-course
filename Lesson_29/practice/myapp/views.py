from django.shortcuts import render
from django.http import HttpResponse

# объект запроса
# контекст

CONTEXT = {

}


def index(request):
    """Homepage view"""
    return HttpResponse("Homepage")


def about(request):
    """About page view"""

    return HttpResponse("About")


def random_id(request, slug):
    context = {
        "id": 1,
        "slug": slug
    }
    return render(request, "base.html", context)
#
#
# def random_id(request, id):
#     # return HttpResponse(f"Random {slug}")
#     context = {
#         "id": id,
#         "slug": "slug"
#     }
#     return render(request, "base.html", context)
