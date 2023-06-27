from django import forms
from .models import SubscribedUsers


class SubscribeForm(forms.ModelForm):
    """ Create form based on SubscribedUsers model """

    class Meta:
        model = SubscribedUsers
        fields = ('name', 'email',)

    def __init__(self, *args, **kwargs):
        """ Adds placeholders and classes """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        self.fields['name'].widget.attrs['aria-label'] = 'Full Name'
        self.fields['email'].widget.attrs['aria-label'] = 'Email Address'

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False
