# Generated by Django 4.0.4 on 2022-04-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_relationship'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='holiday',
            field=models.TextField(default='no holiday', max_length=300),
        ),
    ]
