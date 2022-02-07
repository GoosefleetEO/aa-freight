# Generated by Django 3.2.11 on 2022-02-03 20:35
# Manually combined with a fresh intial migration to eliminate migration issue

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [
        ("freight", "0001_initial_new"),
        ("freight", "0002_auto_20191015_1229"),
        ("freight", "0003_auto_20191028_1023"),
        ("freight", "0004_remove_contract_price"),
        ("freight", "0005_auto_20191028_2155"),
        ("freight", "0006_auto_20191028_2204"),
        ("freight", "0007_auto_20191029_1803"),
        ("freight", "0008_auto_20191030_1547"),
        ("freight", "0009_auto_20191030_2046"),
        ("freight", "0010_auto_20191108_2220"),
        ("freight", "0011_contractcustomernotification"),
        ("freight", "0012_auto_20191210_1406"),
        ("freight", "0013_auto_20191214_1522"),
        ("freight", "0014_auto_20191214_1712"),
        ("freight", "0015_auto_20200130_2328"),
        ("freight", "0016_default_pricing"),
        ("freight", "0017_add_indices"),
    ]

    initial = True

    dependencies = [
        ("authentication", "0019_merge_20211026_0919"),
        ("eveonline", "0015_factions"),
    ]

    operations = [
        migrations.CreateModel(
            name="Freight",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "permissions": (
                    ("add_location", "Can add / update locations"),
                    ("basic_access", "Can access this app"),
                    ("setup_contract_handler", "Can setup contract handler"),
                    ("use_calculator", "Can use the calculator"),
                    ("view_contracts", "Can view the contracts list"),
                    ("view_statistics", "Can view freight statistics"),
                ),
                "managed": False,
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="EveEntity",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        primary_key=True,
                        serialize=False,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("alliance", "Alliance"),
                            ("corporation", "Corporation"),
                            ("character", "Character"),
                        ],
                        max_length=32,
                    ),
                ),
                ("name", models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        help_text="Eve Online location ID, either item ID for stations or structure ID for structures",
                        primary_key=True,
                        serialize=False,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "category_id",
                    models.PositiveIntegerField(
                        choices=[(3, "station"), (65, "structure"), (0, "(unknown)")],
                        default=0,
                        help_text="Eve Online category ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="In-game name of this station or structure",
                        max_length=100,
                    ),
                ),
                (
                    "solar_system_id",
                    models.PositiveIntegerField(
                        blank=True,
                        default=None,
                        help_text="Eve Online solar system ID",
                        null=True,
                    ),
                ),
                (
                    "type_id",
                    models.PositiveIntegerField(
                        blank=True,
                        default=None,
                        help_text="Eve Online type ID",
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pricing",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "collateral_min",
                    models.BigIntegerField(
                        blank=True,
                        default=None,
                        help_text="Minimum required collateral in ISK",
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "collateral_max",
                    models.BigIntegerField(
                        blank=True,
                        default=None,
                        help_text="Maximum allowed collateral in ISK",
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "days_to_expire",
                    models.PositiveIntegerField(
                        blank=True,
                        default=None,
                        help_text="Recommended days for contracts to expire",
                        null=True,
                        validators=[django.core.validators.MinValueValidator(1)],
                    ),
                ),
                (
                    "days_to_complete",
                    models.PositiveIntegerField(
                        blank=True,
                        default=None,
                        help_text="Recommended days for contract completion",
                        null=True,
                        validators=[django.core.validators.MinValueValidator(1)],
                    ),
                ),
                (
                    "details",
                    models.TextField(
                        blank=True,
                        default=None,
                        help_text="Text with additional instructions for using this pricing",
                        null=True,
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Non active pricings will not be used or shown",
                    ),
                ),
                (
                    "is_default",
                    models.BooleanField(
                        default=False,
                        help_text="The default pricing will be preselected in the calculator. Please make sure to only mark one pricing as default.",
                    ),
                ),
                (
                    "is_bidirectional",
                    models.BooleanField(
                        default=True,
                        help_text="Whether this pricing is valid for contracts in either direction or only the one specified",
                    ),
                ),
                (
                    "price_base",
                    models.FloatField(
                        blank=True,
                        default=None,
                        help_text="Base price in ISK",
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "price_min",
                    models.FloatField(
                        blank=True,
                        default=None,
                        help_text="Minimum total price in ISK",
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "price_per_volume",
                    models.FloatField(
                        blank=True,
                        default=None,
                        help_text="Add-on price per m3 volume in ISK",
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "price_per_collateral_percent",
                    models.FloatField(
                        blank=True,
                        default=None,
                        help_text="Add-on price in % of collateral",
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "volume_max",
                    models.FloatField(
                        blank=True,
                        default=None,
                        help_text="Maximum allowed volume in m3",
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "volume_min",
                    models.FloatField(
                        blank=True,
                        default=None,
                        help_text="Minimum allowed volume in m3",
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "use_price_per_volume_modifier",
                    models.BooleanField(
                        default=False,
                        help_text="Whether the global price per volume modifier is used",
                    ),
                ),
                (
                    "end_location",
                    models.ForeignKey(
                        help_text="Destination station or structure for courier route",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="freight.location",
                    ),
                ),
                (
                    "start_location",
                    models.ForeignKey(
                        help_text="Starting station or structure for courier route",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="freight.location",
                    ),
                ),
            ],
            options={
                "unique_together": {("start_location", "end_location")},
            },
        ),
        migrations.CreateModel(
            name="Contract",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("contract_id", models.IntegerField()),
                ("collateral", models.FloatField()),
                (
                    "date_accepted",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                (
                    "date_completed",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                ("date_expired", models.DateTimeField()),
                ("date_issued", models.DateTimeField()),
                (
                    "date_notified",
                    models.DateTimeField(
                        blank=True,
                        db_index=True,
                        default=None,
                        help_text="datetime of latest notification, None = none has been sent",
                        null=True,
                    ),
                ),
                ("days_to_complete", models.IntegerField()),
                ("for_corporation", models.BooleanField()),
                (
                    "issues",
                    models.TextField(
                        blank=True,
                        default=None,
                        help_text="List or price check issues as JSON array of strings or None",
                        null=True,
                    ),
                ),
                ("reward", models.FloatField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("outstanding", "outstanding"),
                            ("in_progress", "in progress"),
                            ("finished_issuer", "finished issuer"),
                            ("finished_contractor", "finished contractor"),
                            ("finished", "finished"),
                            ("canceled", "canceled"),
                            ("rejected", "rejected"),
                            ("failed", "failed"),
                            ("deleted", "deleted"),
                            ("reversed", "reversed"),
                        ],
                        db_index=True,
                        max_length=32,
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True, default=None, max_length=100, null=True
                    ),
                ),
                ("volume", models.FloatField()),
                (
                    "acceptor",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        help_text="character of acceptor or None if accepted by corp",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts_acceptor",
                        to="eveonline.evecharacter",
                    ),
                ),
                (
                    "acceptor_corporation",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        help_text="corporation of acceptor",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts_acceptor_corporation",
                        to="eveonline.evecorporationinfo",
                    ),
                ),
                (
                    "end_location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts_end_location",
                        to="freight.location",
                    ),
                ),
                (
                    "issuer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts_issuer",
                        to="eveonline.evecharacter",
                    ),
                ),
                (
                    "issuer_corporation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts_issuer_corporation",
                        to="eveonline.evecorporationinfo",
                    ),
                ),
                (
                    "pricing",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        related_name="contracts",
                        to="freight.pricing",
                    ),
                ),
                (
                    "start_location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts_start_location",
                        to="freight.location",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ContractHandler",
            fields=[
                (
                    "organization",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="freight.eveentity",
                    ),
                ),
                (
                    "operation_mode",
                    models.CharField(
                        default="my_alliance",
                        help_text="defines what kind of contracts are synced",
                        max_length=32,
                    ),
                ),
                (
                    "price_per_volume_modifier",
                    models.FloatField(
                        blank=True,
                        default=None,
                        help_text="global modifier for price per volume in percent, e.g. 2.5 = +2.5%",
                        null=True,
                    ),
                ),
                (
                    "version_hash",
                    models.CharField(
                        blank=True,
                        default=None,
                        help_text="hash to identify changes to contracts",
                        max_length=32,
                        null=True,
                    ),
                ),
                (
                    "last_sync",
                    models.DateTimeField(
                        blank=True,
                        default=None,
                        help_text="when the last sync happened",
                        null=True,
                    ),
                ),
                (
                    "last_error",
                    models.IntegerField(
                        choices=[
                            (0, "No error"),
                            (1, "Invalid token"),
                            (2, "Expired token"),
                            (3, "Insufficient permissions"),
                            (4, "No character set for fetching alliance contacts"),
                            (5, "ESI API is currently unavailable"),
                            (6, "Operaton mode does not match with current setting"),
                            (99, "Unknown error"),
                        ],
                        default=0,
                        help_text="error that occurred at the last sync atttempt (if any)",
                    ),
                ),
                (
                    "character",
                    models.ForeignKey(
                        default=None,
                        help_text="character used for syncing contracts",
                        null=True,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        related_name="+",
                        to="authentication.characterownership",
                    ),
                ),
            ],
            options={
                "verbose_name": "Contract Handler",
                "verbose_name_plural": "Contract Handler",
            },
        ),
        migrations.CreateModel(
            name="ContractCustomerNotification",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("outstanding", "outstanding"),
                            ("in_progress", "in progress"),
                            ("finished_issuer", "finished issuer"),
                            ("finished_contractor", "finished contractor"),
                            ("finished", "finished"),
                            ("canceled", "canceled"),
                            ("rejected", "rejected"),
                            ("failed", "failed"),
                            ("deleted", "deleted"),
                            ("reversed", "reversed"),
                        ],
                        db_index=True,
                        max_length=32,
                    ),
                ),
                (
                    "date_notified",
                    models.DateTimeField(help_text="datetime of notification"),
                ),
                (
                    "contract",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customer_notifications",
                        to="freight.contract",
                    ),
                ),
            ],
            options={
                "unique_together": {("contract", "status")},
            },
        ),
        migrations.AddField(
            model_name="contract",
            name="handler",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contracts",
                to="freight.contracthandler",
            ),
        ),
        migrations.AddIndex(
            model_name="contract",
            index=models.Index(fields=["status"], name="freight_con_status_b4eb08_idx"),
        ),
        migrations.AlterUniqueTogether(
            name="contract",
            unique_together={("handler", "contract_id")},
        ),
    ]
