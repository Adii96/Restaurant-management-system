# Generated by Django 3.2.12 on 2022-04-11 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restauracja_app', '0014_auto_20220410_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve',
            name='realized',
            field=models.BooleanField(default=False),
        ),
    ]