# Generated by Django 4.0.4 on 2022-06-04 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AvailableTables',
            new_name='AvailableTable',
        ),
    ]