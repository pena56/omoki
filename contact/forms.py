from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control",
    'id': "subject"}), required=True)
    your_email = forms.EmailField(widget=forms.TextInput(attrs={'class': "form-control",
    'id': "email"}), required=True)
    your_message = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control md-textarea",
    'id': "message", 'rows': '2'}), required=True)