# Generated by Django 4.1.7 on 2023-11-19 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livrep', '0003_alter_user_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
    ]