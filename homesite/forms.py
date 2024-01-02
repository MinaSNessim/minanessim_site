from django import forms
from .models import SubscribeToNewsletter, Contact, Portfolio
from ckeditor.widgets import CKEditorWidget


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = SubscribeToNewsletter
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email',
                                             'style': "border-radius: 50px; border-top-right-radius: 0px; "
                                                      "border-bottom-right-radius: 0px; borders:1px"})
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': "borders:1px", 'id': "contact_name"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': "borders:1px"}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'style': "borders:1px"}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'style': "borders:1px"}),
        }


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'body']
