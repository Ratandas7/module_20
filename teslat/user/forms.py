from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'id' : 'required'}))
    email = forms.EmailField(required=True)
    usable_password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if 'usable_password' in self.fields:
    #         del self.fields['usable_password']

class ChangeUserForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email = forms.EmailField(required=True)
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = "__all__"
