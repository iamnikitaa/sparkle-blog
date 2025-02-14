from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from blog.models import Post
import markdown

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:  # An inner class used to define metadata for a model or a form
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:  # An inner class used to define metadata for a model or a form
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        return markdown.markdown(content)  # Converts Markdown to HTML