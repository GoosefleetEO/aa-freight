# Generated by Django 2.2.5 on 2019-10-04 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jfservice', '0003_auto_20191004_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricing',
            name='name',
        ),
    ]
