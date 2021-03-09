from django import forms
from .models import Snippet, Profile

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', 'code', 'language']



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'username', 'user_image']