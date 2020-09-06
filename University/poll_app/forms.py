from django import forms
from poll_app.models import Instructors,userProfileInfo,Questions,Answers
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password',)

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = userProfileInfo
        fields = ('portfolio_site','profile_pic')


class Questionform(forms.ModelForm):

    class Meta:
        model = Questions
        fields = ('Title','Description')

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answers
        fields = '__all__'
# class RegisterationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     class Meta:
#         model = Instructors
#         fields = ('FirstName','LastName','Email')
