from django.db import models
from Psychologist.models import Psychologist
from Authorization.models import User
from django.db.models.signals import post_delete
from django.contrib import admin

'''
class Media(models.Model):
    pass


class Reference(models.Model):
    pass
# Create your models here.

'''


# ГДЕ ПИШУТСЯ СОБСТВЕННЫЕ ВАЛИДАТОРЫ?

class Location(models.Model):
    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адрес'

    address = models.CharField(max_length=248, help_text="Введите в виде: ул., д., к., каб.", blank=False, null=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.address


class Consultation(models.Model):
    class Meta:
        verbose_name = 'Консультация'
        verbose_name_plural = 'Консультация'

    date = models.DateField(blank=False, null=False)
    time = models.CharField(max_length=5, blank=False, null=False)
    id_locations = models.ForeignKey(Location, blank=False, null=False, on_delete=models.DO_NOTHING,
                                     verbose_name='Адрес')
    id_psychologist = models.ForeignKey(Psychologist, blank=False, null=False, on_delete=models.DO_NOTHING,
                                        verbose_name='Психолог')
    is_busy = models.BooleanField(default=False, verbose_name='Занято')

    def __str__(self):
        return f'{self.date.strftime("%d.%m.%Y")}, {self.time}, {self.id_locations.address}, {self.id_psychologist} {"Занято" if self.is_busy else "Свободно"}'


class Appointment(models.Model):
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Запись'

    full_time = 'очно'
    online = 'онлайн'
    choicesformat = [
        ('', '-----'),
        (full_time, 'очно'),
        (online, 'онлайн')
    ]

    id_consultation = models.ForeignKey(Consultation, blank=False, null=False, on_delete=models.DO_NOTHING)
    id_user = models.ForeignKey(User, help_text="Если поле пустое, значит записался неавторизованный пользователь",
                                blank=True, null=True, on_delete=models.DO_NOTHING)
    format = models.CharField(max_length=10, help_text="очно/онлайн", choices=choicesformat,
                              blank=False, null=False)

    def __str__(self):
        return self.id_consultation.id_psychologist.surname

    def get_absolute_url(self):
        return f'/main'

#
# def del_appoi(sender, **kwargs):
#     if kwargs['deleted']:
#         consultation = Consultation
#
#
# post_delete.connect(del_appoi, sender=Appointment)