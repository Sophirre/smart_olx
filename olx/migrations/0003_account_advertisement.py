# Generated by Django 4.0.3 on 2022-03-13 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0002_remove_account_advertisement'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='advertisement',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='account', to='olx.advertisement'),
            preserve_default=False,
        ),
    ]
