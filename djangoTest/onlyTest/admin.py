from django.contrib import admin
from onlyTest.models import *
# Register your models here.

class   bookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pubData']

class   heroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'content', 'gender', 'book']

admin.site.register(bookInfo,bookInfoAdmin)
admin.site.register(heroInfo,heroInfoAdmin)
