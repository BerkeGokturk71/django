from django import forms
from .models import Denek

class DenekForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class" : "form-input",
        "placeholder" : "First Name"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class" : "form-input",
        "placeholder" : "Your Mail"
    }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        "class":"form-input",
        "placeholder" : "messages here"

    }))


    class Meta:
        model = Denek
        fields = ["name","email","text"]
