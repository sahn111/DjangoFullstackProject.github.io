from django import forms

class SendEmail(forms.Form):
    email = forms.EmailField(label = "Email Address")
    rate = forms.CharField(widget=forms.HiddenInput())
