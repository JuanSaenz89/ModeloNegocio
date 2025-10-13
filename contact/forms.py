from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name',required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your name here...'
        }
    ))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your email here...'

        }
    ))
    message = forms.CharField(label='Message',required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Your message here...',
            'maxlength': 750
        }
    ))