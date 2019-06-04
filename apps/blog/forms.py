
from django.contrib.auth.forms import UserCreationForm
from .models import User

from django import forms

from markdown_editor.forms import MarkdownField


class BlogForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    context = MarkdownField()

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")