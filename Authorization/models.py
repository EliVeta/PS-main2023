from django.db import models
from django.contrib.auth.models import User as authUser


class User(models.Model):
    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

    password = models.CharField(max_length=128, blank=False, null=False)
    last_login = models.DateTimeField(auto_now=True, help_text="Дата последнего входа")
    surname = models.CharField(max_length=128, help_text="Фамилия", blank=False, null=False)
    name = models.CharField(max_length=128, help_text="Имя", blank=False, null=False)
    institute = models.CharField(max_length=128,
                                 help_text="Введите полное название, например, Космических и информационных технологий",
                                 blank=True, null=True)
    email = models.EmailField(max_length=256, unique=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True, help_text="Дата первого входа")

    def __str__(self):
        return self.email


class Right(models.Model):
    class Meta:
        verbose_name = 'Права'
        verbose_name_plural = 'Права'

    name = models.CharField(max_length=32, blank=False, null=False)
    default_state = models.BooleanField(default=False, help_text="True — полный запрет на право")

    def __str__(self):
        return self.name


class UserRight(models.Model):
    class Meta:
        verbose_name = 'Права пользователя'
        verbose_name_plural = 'Права пользователя'

    id_right = models.ForeignKey(Right, blank=False, null=False, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    actual_state = models.BooleanField(default=True, help_text="False — запрет права для пользователя")

    def __str__(self):
        return self.id_user.email, self.id_right.name


class UserExtended(models.Model):
    id_user = models.OneToOneField(authUser, blank=False, null=False, on_delete=models.CASCADE, primary_key=True)
    institute = models.CharField(max_length=128,
                                 help_text="Введите полное название, например, Космических и информационных технологий",
                                 blank=True, null=True)

    def __str__(self):
        return self.id_user.email, self.institute
