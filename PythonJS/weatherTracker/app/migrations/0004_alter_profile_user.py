# Generated by Django 5.1.2 on 2024-10-17 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.TextField(default='', max_length=250),
        ),
    ]