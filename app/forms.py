from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, SetPasswordForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer

# import django.contrib.auth.forms as tf
# print('============================')
# print(dir(tf))
# print('============================')



class CustomerRegistrationForm(UserCreationForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
	email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
	class Meta:
		model = User
		fields = ['username','email','password1','password2']
		widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}
		labels = {'email':'Email','username':'UserName'}

class LoginForm(AuthenticationForm):
	username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
	password = forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

# class MyPasswordChangeForm(PasswordChangeForm):
# 	old_password = forms.CharField(label=_("Old Password"),strip=False, widget=forms.PasswordInput(
# 					attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))

# 	new_passrord1 = forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(
# 					attrs={'autocomplete':'new-password','autofocus':True,'class':'form-control'}),
# 					help_text=password_validation.password_validators_help_text_html())

# 	new_passrord2 = forms.CharField(label=_("Confirm New Password"),strip=False,widget=forms.PasswordInput(
# 					attrs={'autocomplete':'new-password','autofocus':True,'class':'form-control'}))

class MyPasswordChangeForm(PasswordChangeForm):
	error_css_class = 'has-error'
	error_messages = {'password_incorrect':_("Your old password was entered incorrectly. Please enter it again."), 'password_mismatch':_("The two password fields didn't match.")}
	old_password = forms.CharField(required=True, label=_('Old Password'),widget=forms.PasswordInput(attrs={'class': 'form-control'}),
					error_messages={'required':_('This field is required')})
	
	new_password1 = forms.CharField(required=True, label=_('New Password'),widget=forms.PasswordInput(attrs={'class': 'form-control'}),
					help_text=password_validation.password_validators_help_text_html(),error_messages={'required':_('This field is required')})#error_messages={'required': 'New Password Required'},

	new_password2 = forms.CharField(required=True, label=_('New Password Confirmation'),widget=forms.PasswordInput(attrs={'class': 'form-control'}),
					help_text=_("Enter the same password as before, for verification."),error_messages={'required':_('This field is required')})#error_messages={'required': 'New Password Confirmation Required'},


class MyPasswordResetForm(PasswordResetForm):
	email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))

class MySetPasswrodForm(SetPasswordForm):
	# new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),
	# 				help_text=password_validation.password_validators_help_text_html())
	# new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))

	new_password1 = forms.CharField(required=True, label=_('New Password'),widget=forms.PasswordInput(attrs={'class': 'form-control'}),
					help_text=password_validation.password_validators_help_text_html(),error_messages={'required':_('This field is required')})#error_messages={'required': 'New Password Required'},

	new_password2 = forms.CharField(required=True, label=_('New Password Confirmation'),widget=forms.PasswordInput(attrs={'class': 'form-control'}),
					help_text=_("Enter the same password as before, for verification."),error_messages={'required':_('This field is required')})#error_messages={'required': 'New Password Confirmation Required'},

class CustomerProfileForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ['name', 'locality', 'city', 'state', 'zipcode']
		widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),'locality':forms.TextInput(attrs={'class':'form-control'}),
					'city':forms.TextInput(attrs={'class':'form-control'}),'state':forms.Select(attrs={'class':'form-control'}),
					'zipcode':forms.NumberInput(attrs={'class':'form-control'})}

