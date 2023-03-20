from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class" : "form-input",
        "placeholder" : "First Name"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class" : "form-input",
        "placeholder" : "Your Mail"
    }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        "class":"form-input",
        "palceholder":"messages"

    }))


    class Meta:
        model = Contact
        fields = ["first_name","email","text"]
