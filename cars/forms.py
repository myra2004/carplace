from django import forms

from cars.models import Brand


class ContactMessageForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


class SearchBrandForm(forms.Form):
    brand = forms.ModelChoiceField(queryset=Brand.objects.all())