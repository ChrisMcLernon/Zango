# Generated by Django 4.2.8 on 2024-01-08 12:46

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid
import zelthy.apps.dynamic_models.fields
import zelthy.core.storage_utils


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("dynamic_models", "communication_0002_object_uuid"),
    ]

    operations = [
        migrations.CreateModel(
            name="MeetingHostModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "object_uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                (
                    "host_object_uuid",
                    models.UUIDField(blank=True, null=True, unique=True),
                ),
                (
                    "provider_config",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, null=True, verbose_name="Provider config"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="appauth.appusermodel",
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="appauth.appusermodel",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="VideoCallConfigModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "object_uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("key", models.CharField(blank=True, max_length=25, unique=True)),
                ("provider", models.CharField(max_length=25, verbose_name="Provider")),
                ("provider_package_name", models.CharField(max_length=100)),
                (
                    "config",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        verbose_name="Config"
                    ),
                ),
                ("is_default", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="appauth.appusermodel",
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="appauth.appusermodel",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="VideoCallRecordModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "object_uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("key", models.CharField(blank=True, max_length=25, unique=True)),
                ("room_id", models.CharField(blank=True, max_length=100)),
                (
                    "participants",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, null=True, verbose_name="Participants"
                    ),
                ),
                (
                    "meeting_details",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, null=True, verbose_name="Meeting details"
                    ),
                ),
                (
                    "scheduled_at",
                    models.DateTimeField(null=True, verbose_name="Scheduled Time"),
                ),
                (
                    "start_time",
                    models.DateTimeField(null=True, verbose_name="Start Time"),
                ),
                ("end_time", models.DateTimeField(null=True, verbose_name="End Time")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("completed", "Completed"),
                            ("cancelled", "Cancelled"),
                            ("scheduled", "Scheduled"),
                            ("failed", "Failed"),
                        ],
                        default="scheduled",
                        max_length=50,
                        verbose_name="Status",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="appauth.appusermodel",
                    ),
                ),
                (
                    "meeting_host",
                    zelthy.apps.dynamic_models.fields.ZForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dynamic_models.meetinghostmodel",
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="appauth.appusermodel",
                    ),
                ),
                (
                    "videocall_config",
                    zelthy.apps.dynamic_models.fields.ZForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="videocall_config",
                        to="dynamic_models.videocallconfigmodel",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
