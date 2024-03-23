from django import forms
from album.models import albums

class album_forms(forms.ModelForm):
    CHOICES = [
        ("web_design", "Web Design"),
        ("seo", "Search Engine Optimization"),
        ("content_creation", "Content Creation"),
        ("social_media", "Social Media Management"),
        ("branding", "Branding"),
    ]
    class Mata:
        model = albums
        fields = "__all__"
        mul   
      = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=CHOICES
    )
