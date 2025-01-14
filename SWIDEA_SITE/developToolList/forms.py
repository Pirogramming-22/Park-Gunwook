from django import forms
from .models import DevelopTool

class DevelopToolForm(forms.ModelForm):
    class Meta:
        model = DevelopTool
        fields = ['name', 'languageType', 'content']