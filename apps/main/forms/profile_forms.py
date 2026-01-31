from django import forms
from apps.main.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("nickname", "icon", "bio")