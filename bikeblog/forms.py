from django import forms
from django.forms import ModelForm
from .models import Post


class BlogForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'subject', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the post title'}),
            'subject': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the post subject'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the post body'}),
        }
