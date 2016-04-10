import re
from django import forms
from django.contrib.auth.models import User
from .models import Article
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.images import get_image_dimensions
from captcha.fields import ReCaptchaField

class ProfileImageForm(forms.Form):
        image = forms.ImageField(label='Select a profile Image')

class RegistrationForm(forms.Form):
 # registration form in user interface with fields
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
    captcha = ReCaptchaField()
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
class ArticleForm(forms.Form):
 # registration form in user interface with fields
    subject = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("subject"))
    description = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("description"))

# class ArticleEdit(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ('subject','description','image')
#     


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email',)

class UserProfileForm(forms.Form):
    # user_id = IntegerField()
    image   = forms.ImageField()
    # class Meta:
    #     model = UserProfile
    #     fields = ('image',)