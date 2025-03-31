# aquí vamos a crear los formularios para hacer post desde fuera 
# blog/forms.py
from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'content')
