from django import forms
from album.models import albums


class album_forms(forms.ModelForm):
    class Meta:
        model = albums
        fields = "__all__"
