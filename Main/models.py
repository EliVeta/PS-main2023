from django.db import models
from django.contrib.auth.models import User
from Psychologist.models import Psychologist

class CommentsPost(models.Model):

    class Meta:
        db_table = 'comments'
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


    choicesGrade = [
        ('', '-----'),
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5)
    ]

    id_user = models.ForeignKey(User, blank=False, null=True, on_delete=models.DO_NOTHING)
    #id_psychologist = models.OneToOneField(Psychologist, blank=False, null=False, on_delete=models.CASCADE,)
    text = models.TextField("Текст комментария")
    created = models.DateTimeField("Добавлен",auto_now_add=True)
    moder = models.BooleanField(default=False)
    grade = models.CharField(max_length=10, help_text="оценка", choices=choicesGrade,
                             blank=False, null=False)

    def __str__(self): #красивый вывод данных

        return f'{self.text}, {self.created.strftime("%d.%m.%Y")}, {self.id_user}'
