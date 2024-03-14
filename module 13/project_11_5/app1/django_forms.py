from django import forms


class student_form(forms.Form):
    name = forms.CharField(label="Enter Name:")
    _id = forms.IntegerField(label="Enter ID:")
    password = forms.PasswordInput(label="Enter Password:")