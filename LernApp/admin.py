from django.contrib import admin
from .models import Tag, LernKarte, Project

# Register your models here.

admin.site.register(Tag)
admin.site.register(LernKarte)
admin.site.register(Project)
