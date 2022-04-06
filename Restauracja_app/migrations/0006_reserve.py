# Generated by Django 3.2.12 on 2022-03-22 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Restauracja_app', '0005_auto_20220322_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('comment', models.CharField(max_length=300)),
                ('tables', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restauracja_app.table')),
            ],
        ),
    ]