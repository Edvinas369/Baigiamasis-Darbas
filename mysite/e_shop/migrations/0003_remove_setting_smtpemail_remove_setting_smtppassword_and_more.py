# Generated by Django 4.0.5 on 2022-07-19 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop', '0002_remove_setting_fax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='smtpemail',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='smtppassword',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='smtpport',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='smtpserver',
        ),
        migrations.AlterField(
            model_name='setting',
            name='icon',
            field=models.ImageField(blank=True, upload_to='image/'),
        ),
    ]