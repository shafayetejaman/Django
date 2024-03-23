from django import forms
from album.models import albums


class album_forms(forms.ModelForm):
    class Meta:
        model = albums
        fields = "__all__"
        widgets = {
            "release_date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }
