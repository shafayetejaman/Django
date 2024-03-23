from django import forms
from album.models import musicians


class musicians_forms(forms.ModelForm):
    class Meta:
        model = musicians
        fields = "__all__"
       
