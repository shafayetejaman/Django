from django import forms
from datetime import date
from django.forms.widgets import NumberInput
from app1.models import MyDBFormClass

CHOICES = [
    ("web_design", "Web Design"),
    ("seo", "Search Engine Optimization"),
    ("content_creation", "Content Creation"),
    ("social_media", "Social Media Management"),
    ("branding", "Branding"),
]


class MyForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=10,
        widget=forms.TextInput(attrs={"class": "bg-black text-white"}),
    )
    email = forms.EmailField(label="Email", required=False, initial="name@gmail.com")
    log = forms.BooleanField(label="Keep Login", initial=True)
    date = forms.DateField(
        label="Submission Date",
        widget=NumberInput(attrs={"type": "date"}),
        initial=date.today(),
    )
    services = forms.MultipleChoiceField(choices=CHOICES)
    top_service = forms.ChoiceField(label="Top Service", choices=CHOICES)
    include = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=CHOICES
    )
    url = forms.URLField(label="Your Website", required=False)
    profile_img = forms.FileField(label="Upload Your Image", required=False)


class MyDBForm:
    class Meta:
        model = My
