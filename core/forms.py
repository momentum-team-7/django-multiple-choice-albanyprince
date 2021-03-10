from django import forms
from .models import Snippet, Profile

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', 'code', 'language']



class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled=True
        self.fields['user'].widget=forms.HiddenInput()
    class Meta:
        model = Profile
        fields = ['user', 'username', 'user_image']