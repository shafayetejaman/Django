from django import forms

class MyForm(forms.forms):
    name = forms.CharField(max_length=10)