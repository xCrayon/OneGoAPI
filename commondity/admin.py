from django.contrib import admin
from .models import Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'picture_url', 'grade', 'parent_id')
    fields = ('name', 'code', 'picture_url', 'parent', 'grade')


admin.site.register(Category, CategoryAdmin)