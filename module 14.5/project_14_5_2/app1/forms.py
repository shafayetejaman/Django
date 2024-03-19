from django import forms
from datetime import date
from app1.models import MyDBFormClass

class MyDBForm(forms.ModelForm):
    class Meta:
        model = MyDBFormClass
        fields = "__all__"
        labels = {
            "ID": "Enter Your ID:",
            "balance": "Total Fee:",
            "login": "Keep login",
            "website":"Your Company Website"
        }
        widgets = {
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "value": date.today(),
                }
            ),
        }
