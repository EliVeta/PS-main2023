from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User as authUser


class RegisterUserForm(forms.ModelForm):
    field_order = ['name', 'surname', 'institute', 'email', 'password', 'password2']

    password = forms.CharField(
        max_length=128,
        label='Введите пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            }
        )
    )
    password2 = forms.CharField(
        max_length=128,
        label='Подтвердите пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Подтвердите пароль'
            }
        )
    )

    class Meta:
        model = User
        exclude = ['last_login', 'is_active', 'date_joined']
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'institute': 'Институт (для студентов)',
            'email': 'E-mail',
        }

class LoginForm(AuthenticationForm):


    username = forms.CharField(
        label='E-mail',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Пример: roma@mail.ru',
                'class': 'form-input'
            }
        )
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Введите пароль',
                'class': 'form-input'
            }
        )
    )


class RegisterSignupForm(UserCreationForm):
    last_name = forms.CharField(
        label="Фамилия",
        widget=forms.TextInput(
            attrs={}
        )
    )
    first_name = forms.CharField(
        label="Имя",
        widget=forms.TextInput(
            attrs={}
        )
    )

    username = forms.CharField(
        label="E-mail",
        widget=forms.EmailInput(
            attrs={'placeholder': 'Например, lizz@mail.ru',}
        )
    )
    password1 = forms.CharField(
        label="Придумайте пароль",
        widget=forms.PasswordInput(
            attrs={}
        )
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput(
            attrs={}
        )
    )

    class Meta:
        model = authUser
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

        '''
        @transaction.atomic
        def save(self):
            user = super().save(commit=False)
            user.is_client = True
            user.save()
            Client.objects.create(user=user,
                                  entity=self.cleaned_data.get('entity'),
                                  address=self.cleaned_data.get('address'),
                                  mode=self.cleaned_data.get('mode'))
            return user
        '''

class ExtendedRegisterSignupForm(forms.ModelForm):
    field_order = ['institute']

    class Meta:
        model = UserExtended
        exclude = ['id_user']
        labels = {
            'institute': 'Можете ввести свой институт (для студентов и сотрудников)'
        }
