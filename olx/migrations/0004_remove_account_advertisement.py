# Generated by Django 4.0.3 on 2022-03-13 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0003_account_advertisement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='advertisement',
        ),
    ]
