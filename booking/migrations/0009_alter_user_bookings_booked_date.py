# Generated by Django 4.0.4 on 2022-06-15 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_alter_user_bookings_booked_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_bookings',
            name='booked_date',
            field=models.DateField(),
        ),
    ]
