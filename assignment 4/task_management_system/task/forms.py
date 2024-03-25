from django import forms
from datetime import date
from .models import Task


class TaskForms(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

        widgets = {
            "date_assigned": forms.DateInput(
                attrs={
                    "type": "date",
                    "value": date.today(),
                }
            ),
        }
