from .models import Comment
from django import forms

#Comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
