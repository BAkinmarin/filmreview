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
