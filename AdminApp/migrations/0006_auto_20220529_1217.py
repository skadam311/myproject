# Generated by Django 2.0.5 on 2022-05-29 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0005_auto_20220529_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventlist',
            name='ticket_amount',
        ),
        migrations.AddField(
            model_name='eventlist',
            name='tickt_amount',
            field=models.IntegerField(default=200, null=True),
        ),
    ]
