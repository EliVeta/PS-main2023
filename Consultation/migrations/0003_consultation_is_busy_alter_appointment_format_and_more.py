# Generated by Django 4.0.4 on 2022-05-22 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Psychologist', '0002_psychologist_profinterests'),
        ('Consultation', '0002_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='is_busy',
            field=models.BooleanField(default=False, verbose_name='Занято'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='format',
            field=models.CharField(choices=[('', '-----'), ('очно', 'очно'), ('онлайн', 'онлайн')], help_text='очно/онлайн', max_length=10),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='id_locations',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Consultation.location', verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='id_psychologist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Psychologist.psychologist', verbose_name='Психолог'),
        ),
    ]