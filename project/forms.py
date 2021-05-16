from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput

from project.models import Category


class CategoryForm(forms.Form):
   name = forms.CharField(min_length=2, max_length=10,
                          required=True, label='Категория',
                          widget=TextInput(
                             attrs={
                                'placeholder': 'Название категории'
                             }
                          ))

   def clean_name(self):
       name = self.cleaned_data['name']
       print(name)
       categories = Category.objects.filter(name=name)
       if categories.count()>0:
           raise ValidationError('Такая категория уже существует')
       return name