from django import forms
from .models import *


class PsychologistForm(forms.ModelForm):
    class Meta:
        model = Psychologist
        fields = ['photo', 'surname', 'name', 'patronymic', 'experience',
                  'education']
        labels = {
             "photo": "Фото психолога",
             "surname": "Фамилия",
             "name": "Имя",
             "patronymic": "Отчество",
             "experience": "Стаж",
             "education": "Образование"
        }


class UrlToOnlineConsultationForm(forms.ModelForm):
    class Meta:
        model = UrlToOnlineConsultation
        fields = ['url']
        exclude = ['id_psychologist'] #мы будем брать данные с таблицы Psychologist
                    #если будет заполнена в форме графа с ссылкой
        labels = {
            "url": "Ссылка на онлайн консультацию"
        }




