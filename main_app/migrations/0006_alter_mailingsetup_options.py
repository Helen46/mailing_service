# Generated by Django 4.2.2 on 2024-11-03 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_client_owner_mailingmessage_owner_mailingsetup_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailingsetup',
            options={'ordering': ('start',), 'permissions': [('block_user', 'Can block user'), ('disable_mailings', 'Can disable mailings')], 'verbose_name': 'Настройка рассылки', 'verbose_name_plural': 'Настройки рассылок'},
        ),
    ]