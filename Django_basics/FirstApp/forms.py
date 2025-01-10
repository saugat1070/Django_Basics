from django import forms
from django.core.exceptions import ValidationError
class StudentForm(forms.Form):
    stname = forms.CharField()
    stadd = forms.CharField()
    stno = forms.IntegerField()
    esal = forms.FloatField()

    def cleanstname(self):
        input_name = forms.clean_data['stname']
        if len(input_name) < 3 and len(input_name) > 10:
            raise ValidationError('Character of name shuold be grater than 3 and less than 10')
        
        return input_name

class form_submission(forms.Form):
    user_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), max_length=30)