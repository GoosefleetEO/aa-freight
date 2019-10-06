# Generated by Django 2.2.5 on 2019-10-06 19:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freight', '0002_pricing_volume_min'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='freight',
            options={'default_permissions': (), 'managed': False, 'permissions': (('add_location', 'Can add / update locations'), ('basic_access', 'Can access this app'), ('setup_contract_handler', 'Can setup contract handler'), ('use_calculator', 'Can use the calculator'), ('view_contracts', 'Can view the contracts list'), ('view_statistics', 'Can view freight statistics'))},
        ),
        migrations.RemoveField(
            model_name='contract',
            name='date_notified',
        ),
        migrations.AddField(
            model_name='contract',
            name='issues',
            field=models.TextField(default=None, help_text='List or price check issues as JSON array of strings or None', null=True),
        ),
        migrations.AddField(
            model_name='contracthandler',
            name='send_notifications',
            field=models.BooleanField(default=False, help_text='Switch to activate/deactivate the sending of notifications'),
        ),
        migrations.AlterField(
            model_name='contracthandler',
            name='last_error',
            field=models.IntegerField(choices=[(0, 'No error'), (1, 'Invalid token'), (2, 'Expired token'), (3, 'Insufficient permissions'), (4, 'No character set for fetching alliance contacts'), (5, 'ESI API is currently unavailable'), (99, 'Unknown error')], default=0, help_text='error that occurred at the last sync atttempt (if any)'),
        ),
        migrations.AlterField(
            model_name='contracthandler',
            name='last_sync',
            field=models.DateTimeField(blank=True, default=None, help_text='when the last sync happened', null=True),
        ),
        migrations.AlterField(
            model_name='contracthandler',
            name='version_hash',
            field=models.CharField(blank=True, default=None, help_text='hash to identify changes to contracts', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='category_id',
            field=models.IntegerField(choices=[(3, 'station'), (65, 'structure'), (0, '(unknown)')], default=0, help_text='Eve Online category ID', validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.BigIntegerField(help_text='Eve Online location ID, either item ID for stations or structure ID for structures', primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(help_text='In-game name of this station or structure', max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='solar_system_id',
            field=models.IntegerField(blank=True, default=None, help_text='Eve Online solar system ID', null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='location',
            name='type_id',
            field=models.IntegerField(blank=True, default=None, help_text='Eve Online type ID', null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
