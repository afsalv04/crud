from django import forms
from .models import anim 

class animForm(forms.ModelForm):
    class Meta:
        model = anim
        fields = ['name', 'species', 'age', 'ownername']
