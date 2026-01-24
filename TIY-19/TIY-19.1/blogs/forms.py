from django import forms

from .models import BlogPost

class BlogForm(forms.ModelForm):
    """Form for entering new blogs"""
    class Meta:
        """Decide on what to show in a form"""
        model = BlogPost
        fields = ['title','text']
        label = {'title':'blog title',}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}