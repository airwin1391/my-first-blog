from django import forms
from .models import Post

# Creating form called PostForm then tell Django that the
# form is a ModelForm
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
