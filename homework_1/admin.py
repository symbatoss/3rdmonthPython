from django.contrib import admin

# Register your models here.
from homework_1.models import University, Faculty, Review
admin.site.register(Faculty)
admin.site.register(University)
admin.site.register(Review)
