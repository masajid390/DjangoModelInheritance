from django.contrib import admin
from .models import Cat, Dog


class DogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday')
    fields = ('name', 'birthday')
    ordering = ('name', 'birthday')
    list_editable = ('name', 'birthday')
    search_fields = ('name', 'birthday')
    list_per_page = 20
    list_filter = ['name', 'birthday']


class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday')
    fields = ('name', 'birthday')
    ordering = ('name', 'birthday')
    list_editable = ('name', 'birthday')
    search_fields = ('name', 'birthday')
    list_per_page = 20
    list_filter = ['name', 'birthday']


admin.site.register(Cat, CatAdmin)
admin.site.register(Dog, DogAdmin)
