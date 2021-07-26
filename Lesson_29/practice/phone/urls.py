from django.urls import path, re_path
from phone.views import phone, phone_num10, phone_templates, about

urlpatterns = [
    path("about/", about, name="about"),
    path("<str:phone_num>/", phone_templates, name="phone")
    # path("<str:phone_number>/", phone, name="phone"),
    # re_path(r"(?P<phone_num>380\d{3})", phone_num10, name="pn3"),
    # re_path(r"(?P<phone_num>380\d{10})", phone, name="pn10")
]
