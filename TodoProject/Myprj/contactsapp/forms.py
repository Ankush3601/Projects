from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(label="Enter Name", max_length=250)
    email = forms.EmailField(label="Enter Email")
    password = forms.CharField(label="Enter Password", max_length=250, widget=forms.PasswordInput)
    age = forms.IntegerField(label="Enter Age", help_text="Age Should be in Numbers")
    income = forms.DecimalField(label="Enter Income")
    dateofbirth = forms.DateField(label="Enter DOB", help_text="yyyy-mm-dd")
    photo = forms.FileField(label="Browse picture to upload")
    is_married = forms.BooleanField()
    membershipchoice = [('G', "Gold"), ('S', "Silver"), ('P', "Platinum")]
    memberships = forms.ChoiceField(widget=forms.Select,choices=membershipchoice)