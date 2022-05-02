
from django import forms
from django.forms import HiddenInput


class ContactForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=30,widget=forms.TextInput(attrs={'class':'form__input','id':''}))
    phone = forms.CharField(min_length=11,max_length=16,widget=forms.TextInput(attrs={'class':'form__input','type':'tel','id':''}))
    message = forms.CharField(min_length=4,widget=forms.Textarea(attrs={'class':'form__textarea','required':'required','id':''}))

class BuyForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=30,widget=forms.TextInput(attrs={'class':'form__input','id':''}))
    phone = forms.CharField(min_length=11,max_length=16,widget=forms.TextInput(attrs={'class':'form__input','type':'tel','id':''}))
    email = forms.EmailField(min_length=2,widget=forms.TextInput(attrs={'class':'form__email','id':''}))
    hidden = forms.CharField(widget=HiddenInput(attrs={'class':'hidden-input','id':''}))