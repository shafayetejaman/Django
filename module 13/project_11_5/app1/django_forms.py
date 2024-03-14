from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(label="Enter your Name:")
    _id = forms.IntegerField(label="Enter ID:")
    password = forms.EmailField(label="Enter Email:")
