# Generated by Django 4.2.2 on 2024-11-05 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_mailingsetup_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailingsetup',
            name='next_send',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата следующей отправки'),
        ),
    ]