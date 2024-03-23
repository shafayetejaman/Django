from django import forms
from album.models import albums


class album_forms(forms.ModelForm):
    class Meta:
        models = albums
        fields = "__all__"
