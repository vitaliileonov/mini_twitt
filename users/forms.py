from django import forms
from posts.models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['name', 'title', 'location', 'date_of_birth', 'profile_picture', 'title_picture']
        widgets = {
            'name': forms.Textarea(
                attrs={'class': 'form-control', "rows": "1", 'placeholder': 'Name '}),
            'title': forms.Textarea(
                attrs={'class': 'form-control', "rows": "2", 'placeholder': 'About Me'}),
            'location': forms.Textarea(
                attrs={'class': 'form-control', "rows": "1", 'placeholder': 'Location'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'title_picture': forms.FileInput(attrs={'class': 'form-control'})
        }

