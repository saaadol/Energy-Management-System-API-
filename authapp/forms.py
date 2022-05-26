from django import forms
class UserForm(forms.ModelForm):
    class Meta:
        model = User_Data
        widgets = {
        'password': forms.PasswordInput(),
    }