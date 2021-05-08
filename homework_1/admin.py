from django.contrib import admin

# Register your models here.
from homework_1.models import University, Faculty, Review


class UniversityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Faculty)
admin.site.register(Review)
admin.site.register(University, UniversityAdmin)

