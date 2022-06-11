# Generated by Django 4.0.4 on 2022-06-04 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableTables',
            fields=[
                ('booking_date', models.DateField(primary_key=True, serialize=False)),
                ('time_slot_12', models.PositiveSmallIntegerField(default=10)),
                ('time_slot_14', models.PositiveSmallIntegerField(default=10)),
                ('time_slot_16', models.PositiveSmallIntegerField(default=10)),
                ('time_slot_18', models.PositiveSmallIntegerField(default=10)),
                ('time_slot_20', models.PositiveSmallIntegerField(default=10)),
                ('time_slot_22', models.PositiveSmallIntegerField(default=10)),
            ],
        ),
    ]