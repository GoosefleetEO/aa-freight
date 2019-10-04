# Generated by Django 2.2.5 on 2019-10-04 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jfservice', '0005_auto_20191004_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractshandler',
            name='last_sync',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='contractshandler',
            name='version_hash',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='solar_system_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='type_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]