from django import forms
from django.forms import Textarea
from .models import Search


class SearchForm(forms.ModelForm):

    class Meta:
        model = Search
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={'class': 'search-box', 'rows': '1'}),
        }
