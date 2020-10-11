from django.contrib import admin

# Register your models here.
from django.contrib import admin
from practice_app.models import Person


class PersonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person)