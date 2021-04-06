from django.contrib import admin
# from .models import Book, BookNumber, Character, Author
from .models import ccsFormData
# Register your models here.

@admin.register(ccsFormData)
class ccsAdmin(admin.ModelAdmin):
    list_display = ['clientNumber', 'firstName', 'lastName', 'firstNameNOTsame',
                    'lastNameNOTsame', 'nameOtherKnown','namePrefer','dob']
    list_filter = ['clientNumber']
    search_fields = ['clientNumber']



