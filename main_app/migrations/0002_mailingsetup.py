# Generated by Django 4.2.2 on 2024-10-18 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(verbose_name='Дата начала первой рассылки')),
                ('periodicity', models.CharField(choices=[('once', 'Единоразовая'), ('daily', 'Ежедневная'), ('weekly', 'Раз в неделю'), ('monthly', 'Раз в месяц')], default='once', verbose_name='Переодичность рассылки')),
                ('status', models.CharField(choices=[('created', 'Создана'), ('started', 'Запущена'), ('finished', 'Завершена')], default='created', verbose_name='Статус рассылки')),
                ('clients', models.ManyToManyField(related_name='Clients', to='main_app.client')),
            ],
            options={
                'verbose_name': 'Настройка рассылки',
                'verbose_name_plural': 'Настройки рассылок',
                'ordering': ('start',),
            },
        ),
    ]
