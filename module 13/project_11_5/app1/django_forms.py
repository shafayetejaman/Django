from django import forms


class student_form(forms.Form):
    name = forms.CharField(label="Name")
    _id = forms.IntegerField(label="ID")
    password = forms.PasswordInput()