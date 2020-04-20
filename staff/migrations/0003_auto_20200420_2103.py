# Generated by Django 3.0.5 on 2020-04-20 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20200420_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadence',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='cadence',
            name='end',
            field=models.IntegerField(default=2014, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cadence',
            name='start',
            field=models.IntegerField(default=2020, max_length=4),
            preserve_default=False,
        ),
    ]