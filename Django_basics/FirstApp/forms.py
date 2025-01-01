from django import forms
class StudentForm(forms.Form):
    stname = forms.CharField()
    stadd = forms.CharField()
    stno = forms.IntegerField()
    esal = forms.FloatField()
    
