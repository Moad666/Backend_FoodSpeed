# Generated by Django 4.1.7 on 2023-11-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livrep', '0002_remove_user_is_active_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateField(null=True),
        ),
    ]