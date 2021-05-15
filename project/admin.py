from django.contrib import admin

# Register your models here.
from project.models import Category, Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'category']
    list_editable = ['title', 'price', 'category']
    search_fields = ['title', 'price', 'category']
    list_filter = ['title']


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
