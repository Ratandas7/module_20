from django import forms
from car.models import Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment']
        labels = {
            'comment': 'Review'
        }
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
        }