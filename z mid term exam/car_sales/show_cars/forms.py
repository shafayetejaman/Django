from .models import Car, Brand, Comment
from django import forms


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

class BrandForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        
    def __str__(self) -> str:
       self.name

class CommentForm(forms.ModelForm):
    class Meta:
        model = Car
        fields=["name", "email"]

    def __str__(self) -> str:
        self.name
