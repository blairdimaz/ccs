from django.contrib import admin
# from .models import Book, BookNumber, Character, Author
from .models import ccsFormData, children, parent, ece
# Register your models here.

@admin.register(ccsFormData)
class ccsAdmin(admin.ModelAdmin):
    list_display = ['clientNumber', 'firstName', 'lastName', 'firstNameNOTsame',
                    'lastNameNOTsame', 'nameOtherKnown','namePrefer','dob']
    list_filter = ['clientNumber']
    search_fields = ['clientNumber']

@admin.register(children)
class childAdmin(admin.ModelAdmin):
    list_display = ['child_FullName']
    list_filter = ['child_FullName']
    search_fields = ['child_FullName','child_Parent']

@admin.register(parent)
class parentAdmin(admin.ModelAdmin):
        list_display = ['username']
        list_filter = ['username','children','partner']
        search_fields = ['username','children','partner']

@admin.register(ece)
class eceAdmin(admin.ModelAdmin):
        list_display = ['ECE_Id','Org_Name','Email','Org_Type',
                        'Twenty_Hrs_ECE','Education_Region', 'Contact1_Name']
        list_filter = ['Org_Name']
        search_fields = ['ECE_Id', 'Org_Name']


