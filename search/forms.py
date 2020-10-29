from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class SignUpForm(UserCreationForm): 
        email =  forms.EmailField()
        class Meta:  
            model = User  
            fields = ('username', 'email', 'password1', 'password2')
        def save(self, commit=True):
            user = super(SignUpForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')
        
class ProfileForm(forms.ModelForm):
    class Meta: 
        model = Profile
        fields = ('user',)