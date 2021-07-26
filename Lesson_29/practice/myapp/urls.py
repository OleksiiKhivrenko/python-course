from django.urls import path, re_path
from myapp.views import index, about, random_id

urlpatterns = [
    path("", index, name="index"),
    path("/about", about, name="about"),
    path("<int:id>", random_id, name="id")
]

