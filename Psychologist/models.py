from django.db import models


class Psychologist(models.Model):
    class Meta:
        verbose_name = 'Психологи'
        verbose_name_plural = 'Психологи'

    surname = models.CharField(max_length=128, blank=False, null=False)
    name = models.CharField(max_length=128, blank=False, null=False)
    patronymic = models.CharField(max_length=128, blank=False, null=False)
    experience = models.IntegerField(help_text="Укажите число лет", blank=False, null=False)
    education = models.CharField(max_length=248, blank=False, null=False)
    photo = models.ImageField(upload_to='psychologist/')
    profinterests = models.TextField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.surname + ' ' + self.name


class UrlToOnlineConsultation(models.Model):
    class Meta:
        verbose_name = 'Ссылки для онлайн консультаций'
        verbose_name_plural = 'Ссылки для онлайн консультаций'

    id_psychologist = models.OneToOneField(Psychologist, blank=False, null=False, on_delete=models.CASCADE, primary_key=True)
    url = models.CharField(max_length=248, blank=False, null=False)

    def __str__(self):
        return self.id_psychologist.surname



