from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Review, Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    image = forms.ImageField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'image']
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["título", "avaliação", "detalhes"]
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']