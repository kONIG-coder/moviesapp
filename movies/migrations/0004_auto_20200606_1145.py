# Generated by Django 3.0.7 on 2020-06-06 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20200606_1118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='daily_rate',
            new_name='rating',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='number_in_stock',
        ),
    ]
