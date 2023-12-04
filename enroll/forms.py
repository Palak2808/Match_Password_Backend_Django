from django.core import validators
from django import forms 
class StudentRegisteration(forms.Form):
    name=forms.CharField()
    email= forms.EmailField()
    pas=forms.CharField(widget=forms.PasswordInput)
    pas2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data=super().clean()
        valpwd= self.cleaned_data['pas']
        valpwd2= self.cleaned_data['pas2']
        if valpwd != valpwd2 :
            raise forms.ValidationError('Password doesnt match')