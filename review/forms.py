from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ReviewRequestForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    film_title = forms.CharField(label="Film Title", max_length=200)
    message = forms.CharField(widget=forms.Textarea, label="Why should this be reviewed?")
