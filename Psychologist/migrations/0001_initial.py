# Generated by Django 4.0.3 on 2022-04-07 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Psychologist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('patronymic', models.CharField(max_length=128)),
                ('experience', models.IntegerField(help_text='Укажите число лет')),
                ('education', models.CharField(max_length=248)),
                ('photo', models.ImageField(upload_to='psychologist/')),
            ],
        ),
        migrations.CreateModel(
            name='UrlToOnlineConsultation',
            fields=[
                ('id_psychologist', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Psychologist.psychologist')),
                ('url', models.CharField(max_length=248)),
            ],
        ),
    ]
