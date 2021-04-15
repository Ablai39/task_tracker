from django import forms

class AuthForm(forms.Form):
    email = forms.CharField(required=True, label=u'Логин')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label=u'Пароль')