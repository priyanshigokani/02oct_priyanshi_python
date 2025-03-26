from django.contrib import admin
from .models import *

# Register your models here.

class Dt(admin.ModelAdmin):
    list_display = ["id", "name", "email", "city"]

admin.site.register(info,Dt)

