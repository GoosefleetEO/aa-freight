# Generated by Django 2.2.5 on 2019-10-28 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freight', '0003_auto_20191028_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='price',
        ),
    ]