# Generated by Django 4.0.3 on 2022-05-10 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Right',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('default_state', models.BooleanField(default=False, help_text='True — полный запрет на право')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(auto_now=True, help_text='Дата последнего входа')),
                ('surname', models.CharField(help_text='Фамилия', max_length=128)),
                ('name', models.CharField(help_text='Имя', max_length=128)),
                ('institute', models.CharField(blank=True, help_text='Введите полное название, например, Космических и информационных технологий', max_length=128, null=True)),
                ('email', models.EmailField(max_length=256, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, help_text='Дата первого входа')),
            ],
        ),
        migrations.CreateModel(
            name='UserRight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_state', models.BooleanField(default=True, help_text='False — запрет права для пользователя')),
                ('id_right', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authorization.right')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authorization.user')),
            ],
        ),
    ]
