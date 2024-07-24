# forms.py
from django import forms
from accounts.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['category']  # To include all fields from the Profile model

        widgets = {
            'category' : forms.Select(attrs={'class':'form-control'}),
        }

        labels = {
            'category' : 'Category',
        }