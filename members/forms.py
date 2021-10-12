from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from theblog.models import Profile
from django import forms


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),help_text=None)
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Firstname'}),help_text=None)
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Lastname'}),help_text=None)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),help_text=None) 
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),help_text=None)  
    password2 = forms.CharField(label='Password Again',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password again'}),help_text=None) 
    phoneno = forms.IntegerField(label='Phone No.',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'+91 XXX XXX XXXX'}),help_text=None) 
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','phoneno','password1','password2')



'''
id_last_login
id_is_superuser
id_groups
id_username
id_first_name
id_last_name
id_email
id_is_staff
id_is_active
id_date_joined


'''
class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Old Password'}),help_text=None)
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'New Password'}),help_text=None)
    new_password2 = forms.CharField(label='Password Again',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'New Password Again'}),help_text=None) 
    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')