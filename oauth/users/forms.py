from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    input_class = {"class": "block w-full p-3 pl-6 text-sm text-gray-600 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-400 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"}
    error_messages = {
        'required': 'Обязательное поле',
        'invalid': 'Неверный формат',
        'unique': 'Пользователь с таким логином уже существует',
    }
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs=input_class))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs=input_class))
    # убрать повторный ввод пароля
    password2 = None

    class Meta:
        model = User
        fields = ('username',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data[ "password1" ])
        if commit:
            user.save()
        return user
