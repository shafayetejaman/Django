from django import forms
from album.models import albums

choice = [
    ("web_design", "Web Design"),
    ("seo", "Search Engine Optimization"),
    ("content_creation", "Content Creation"),
    ("social_media", "Social Media Management"),
    ("branding", "Branding"),
]

class album_forms(forms.ModelForm):
    class Meta:
        model = albums
        fields = "__all__"
        widgets = {
            "instrument_type": forms.MultipleChoiceField(
                widget=forms.CheckboxSelectMultiple, choices=choice
            )
        }
