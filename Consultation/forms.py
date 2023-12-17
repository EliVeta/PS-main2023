from django import forms
from .models import *


# Исправить на модель:
class AppointmentConsultationForm(forms.Form):
    # format = forms.NullBooleanField(
    # label = "Формат консультации",
    #    widget = forms.NullBooleanSelect()
    # )

    CHOICESformat = [
        ('full-time', 'очно'),
        ('online', 'онлайн')
    ]
    CHOICESaddress = [('Borisova1', 'ул. Борисова 1'),
                      # С моделью мы будем передавать ID площадки в качестве ключа (значения)
                      ('Svobodnyy79', 'пр. Свобдный 79, ауд. 14-05а'),
                      # и адрес в качестве удобочитаемого для пользователя текста
                      ('Vuzovsky', 'пер. Вузовский 8')]  # результат выбора будет отправляться в БД по ID
    CHOICESspecialist = [('sp1', 'Валерия коновалова'),  # будем получать id в качесве ключа
                         ('sp2', 'Юлия Варфоломеева'),
                         ('sp3', 'Полина Иванникова'),
                         ('sp4', 'Асылбек Умирзаков'),
                         ]
    format = forms.ChoiceField(choices=CHOICESformat, widget=forms.RadioSelect, label='Формат')
    address = forms.ChoiceField(choices=CHOICESaddress, widget=forms.Select, label='Площадка')
    specialist = forms.ChoiceField(choices=CHOICESspecialist, widget=forms.Select,
                                   label='Специалист')  # if address такой-то, то соответствующие ему специалисты
    # в choices передать ФИО (фото) специалиста из таблицы
    years = ['2022']  # получаем после преобразования даты
    months = ['5']
    day = [1, 2, 3, 4, 5]
    date = forms.DateField(widget=forms.SelectDateWidget(years=years),
                           label='Дата')  # будет получать дату в формате datetime
    # видимо разделять и отдельно отображать дату и времена для даты
    # time = format.TimeField()
    # BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    # чтобы поле формы было необязательным, используй required=False

    description = forms.CharField(label="Можете кратко опиcать свою проблему", widget=forms.TextInput, required=False)


class AppointmentForm(forms.ModelForm):
    text = forms.CharField(label='Опишите свою проблему', widget=forms.Textarea(), required=False)

    class Meta:
        model = Appointment
        fields = ['format']
        exclude = ['id_user', 'id_consultation']
        labels = {
            "format": "Формат"
        }

        widgets = {'format': forms.Select(attrs={'onchange': 'ChangeForm()'})}


class ConsultationForm(forms.ModelForm):
    field_order = ["Дата", "Время"]
    date = forms.ChoiceField(label='Дата', widget=forms.Select(attrs={'onchange': 'ChangeForm()'}))
    time = forms.ChoiceField(label='Время', widget=forms.Select(attrs={'onchange': 'ChangeForm()'}))

    class Meta:
        model = Consultation
        fields = '__all__'

        widgets = {
            'id_locations': forms.Select(attrs={'onchange': 'ChangeForm()'}),
            'id_psychologist': forms.Select(attrs={'onchange': 'ChangeForm()'}),
        }


class DataUserForm(forms.Form):
    surname = models.CharField(max_length=128, help_text="Фамилия", blank=False, null=False)
    name = models.CharField(max_length=128, help_text="Имя", blank=False, null=False)
    email = models.EmailField(max_length=256, unique=True)
    description = forms.CharField(label="Можете кратко опиcать свою проблему", widget=forms.TextInput, required=False)
    field_order = ['Фамилия', 'Имя', 'E-mail', 'Можете кратко описать проблему']
