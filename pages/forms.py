from django import forms
from users.models import User


class RegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = {
			'first_name',
			'last_name',
			'user_email',
		}