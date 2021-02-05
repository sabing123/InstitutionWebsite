from django import forms

class ContactForm(forms.Form):
    name= forms.CharField(max_length=500, label="Name")
    email= forms.EmailField(max_length=500, label="Email")
    phone= forms.CharField(max_length=15, label="Phone")
    subject= forms.CharField(max_length=500, label="Subject")
    message= forms.CharField(label='Message',widget=forms.Textarea(
                        attrs={'placeholder': 'Enter your message here'}))