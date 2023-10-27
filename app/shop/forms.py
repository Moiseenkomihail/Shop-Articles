from .models import ProductComent
from django import forms


class ProductCommentForm(forms.ModelForm):

    class Meta:
        model = ProductComent
        fields = ['comment']
        labels = {
            'comment': '',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Comment', 'rows':4, 'cols':50}),
            } 