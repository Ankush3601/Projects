from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    date_of_birth = forms.DateField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
