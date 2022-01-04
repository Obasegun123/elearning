from django.contrib import admin
from .models import Author, Category, Courses,Comment
# Register your models here.

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Courses)
admin.site.register(Comment)