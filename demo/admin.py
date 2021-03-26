from django.contrib import admin
# from .models import Book, BookNumber, Character, Author
from .models import ccsFormData
# Register your models here.

@admin.register(ccsFormData)
class ccsAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']
    list_filter = ['name']
    search_fields = ['name']



