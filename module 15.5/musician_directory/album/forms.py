from django import forms
from album.models import albums

class album_forms(forms.ModelForm):
    class Mata:
        model = albums
        fields = "__all__"