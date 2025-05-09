""" from django import forms
from django.contrib.auth.models import User
from core.models import RoleMaster, CustomUser

from django import forms
from django.contrib.auth.models import User
from core.models import RoleMaster, CustomUser

class UserCreationWithRoleForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ModelChoiceField(queryset=RoleMaster.objects.all(), required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            role = self.cleaned_data['role']
            CustomUser.objects.create(user=user, role=role)
        return user

 """