from django import forms
from members.models import UserProfileInfo
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.IntegerField(label="ID", widget=forms.TextInput(attrs={'class': 'masterclass'}))

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class UserProfileInfoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileInfoForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = UserProfileInfo
        fields = ('first_name', 'last_name', 'leader', 'department', 'post')


