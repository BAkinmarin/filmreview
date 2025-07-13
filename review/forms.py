from .models import Comment, ReviewRequest
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ReviewRequestForm(forms.ModelForm):
    class Meta:
        model = ReviewRequest
        fields = ['name', 'email', 'film_title', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-element'}),
            'email': forms.EmailInput(attrs={'class': 'form-element'}),
            'film_title': forms.TextInput(attrs={'class': 'form-element'}),
            'message': forms.Textarea(attrs={'class': 'form-element', 'rows': 5}),
        }
