import uuid
# timedelta - тупо отчет времени
from datetime import timedelta

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.utils.timezone import now
from users.models import User, EmailVerification


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={

        'class': "form-control py-4",
        'placeholder': 'Введите пароль'

    }))

    class Meta:
        model = User
        fields = ("username", "password")


class UserRegistrationForm(UserCreationForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя'
    }
    ))

    lastname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите фамилию'
    }
    ))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя'
    }
    ))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите адрес эл. почты'
    }
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs=
    {
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль'
    }
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs=
    {
        'class': 'form-control py-4',
        'placeholder': 'Повторите пароль'
    }
    ))

    class Meta:

        model = User
        fields = ('firstname', "lastname", 'username', 'email', 'password1', 'password2')

    #метод срабатывающий при создании
    def save(self, commit=True):

        user = super(UserRegistrationForm, self).save(commit=True)
        # время регистрации + 2 дня
        expiration = now() + timedelta(days=2)
        # uuid.uuid4 - создание уникального кода в формате '9de760c4-da0c-498c-b75d-b228ddd65f38'
        record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expirations=expiration)
        # после создания record используем функцию модели
        record.send_verification_email()

        return user

class UseProfileForm(UserChangeForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
    }))

    lastname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
    }))

    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input',

    }), required= False)

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'readonly': True
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'readonly': True
    }))

    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'image', 'username', 'email')
