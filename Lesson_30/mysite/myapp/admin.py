from django.contrib import admin
from myapp.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name"]

# Register your models here.
