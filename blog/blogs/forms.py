from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'Title of post:', 'text': 'Description of post:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
