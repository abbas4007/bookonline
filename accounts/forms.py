from django import forms
from .models import User, OtpCode,Profile
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
	password1 = forms.CharField(label='password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('email', 'phone_number', 'full_name')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
			raise ValidationError('passwords dont match')
		return cd['password2']

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user


class UserChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField(help_text="you can change password using <a href=\"../password/\">this form</a>.")

	class Meta:
		model = User
		fields = ('email', 'phone_number', 'full_name', 'password', 'last_login')


class UserRegistrationForm(forms.Form):
    full_name = forms.CharField(label='نام کامل')
    email = forms.EmailField(label='ایمیل')
    phone = forms.CharField(label='شماره موبایل', max_length=11)
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)

    city = forms.ChoiceField(choices=Profile.CITY_CHOICES, label='شهر')
    address = forms.CharField(label='آدرس')





class VerifyCodeForm(forms.Form):
	code = forms.IntegerField()


class UserLoginForm(forms.Form):
	phone = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
	class Meta :
		model = Profile
		fields = ['city', 'address']
		widgets = {
			'city' : forms.Select(attrs = {'class' : 'form-select'}),
			'address' : forms.Textarea(attrs = {
				'class' : 'form-control',
				'rows' : 3,
				'placeholder' : 'آدرس کامل (خیابان، کوچه، پلاک، واحد)'
			}),
		}


