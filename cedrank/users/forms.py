from django import forms
from users.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileForm(forms.ModelForm):
     class Meta():
         model = UserProfile
         fields = ('company_name','company_id','phone')