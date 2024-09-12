from .models import Review
from django.forms import ModelForm

class review_form(ModelForm):
    class Meta:
        model=Review
        fields=[
            'value',
            'body'
        ]
        
        labels={
        'value':'Please Vote',
        'body':'Write your review here'
    }
