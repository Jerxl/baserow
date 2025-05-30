# Generated by Django 5.0.13 on 2025-04-16 08:12

import django.db.models.deletion
from django.db import migrations, models

import baserow.core.fields


class Migration(migrations.Migration):
    dependencies = [
        ("baserow_enterprise", "0045_fileinputelement_and_more"),
        ("database", "0187_booleanfield_boolean_default_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="FieldPermissions",
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
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", baserow.core.fields.SyncedDateTimeField(auto_now=True)),
                (
                    "role",
                    models.TextField(
                        choices=[
                            ("BUILDER", "Builder"),
                            ("ADMIN", "Admin"),
                            ("CUSTOM", "Custom"),
                            ("NOBODY", "Nobody"),
                        ],
                        help_text="The minimum role required to update the data of this field. EDITOR is the default role for a field, so it is not necessary to set it, and when reset the field permission will be set to EDITOR. ",
                    ),
                ),
                (
                    "allow_in_forms",
                    models.BooleanField(
                        default=False,
                        help_text="Whether this field can be updated in forms, no matter the permissions set for the field. This is useful for fields that are not editable in the table view, but should be editable in forms.",
                    ),
                ),
                (
                    "field",
                    models.OneToOneField(
                        help_text="The field that this permission applies to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="permission",
                        to="database.field",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
