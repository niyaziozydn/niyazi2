from django.contrib import admin
from .models import Category, Todo, Contact
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title',
        'is_active',
        'category',
    ]
    list_display_links = [
        'pk',
        'title',
        'category',
    ]
admin.site.register(Todo,TodoAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Contact)


