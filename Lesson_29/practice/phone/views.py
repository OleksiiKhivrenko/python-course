from django.http import HttpResponse, Http404
from django.shortcuts import render


class MyClass:
    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar


myClass = MyClass("CLASS FOO", "CLASS BAR")


def phone(request, phone_number):
    """Phone number view"""

    if len(phone_number) == 12 and phone_number.isdigit() and phone_number.startswith("380"):
        return HttpResponse(phone_number)

    raise Http404("not a ukrainian phone number")


def phone_num10(request, phone_num):
    return HttpResponse(f"{phone_num}")


def phone_templates(request, phone_num):
    context = {
        "phone": phone_num,
        "another_number": "123",
        "vodaphone": phone_num.startswith("38095"),
        "list": ["apple", "banana", "nuts", "cherry"],
        "test": myClass.foo
    }
    return render(request, "phone.html", context)


def about(request):
    context = {

    }
    return render(request, "about.html", context)
