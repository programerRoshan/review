from django import forms

from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [ 'Faculty', 'name', 'reviewText']


    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            return 'anonymous'
        else:
            return name
