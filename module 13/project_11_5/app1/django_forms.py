from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(label="Enter your Name:")
    email = forms.EmailField(label="Enter Email:")
