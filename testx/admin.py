from ast import In
from django.contrib import admin
from .models import Enterp, Investor, Forum

# Register your models here.

admin.site.register(Enterp)
admin.site.register(Investor)
admin.site.register(Forum)