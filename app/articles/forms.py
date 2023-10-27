from .models import ArticleComment
from django import forms


class ArticleCommentForm(forms.ModelForm):

    class Meta:
        model = ArticleComment
        fields = ['comment']
        labels = {
            'comment': '',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Comment', 'rows':4, 'cols':50}),
            } 