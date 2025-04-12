from django import forms
from .models import CustomUser,Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','content']



class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='confirm password')

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("password don't matched ")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user

