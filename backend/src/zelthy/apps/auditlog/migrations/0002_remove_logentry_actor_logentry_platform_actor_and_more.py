# Generated by Django 4.2.11 on 2024-03-29 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("platformauth", "0002_platformusermodel_is_superadmin_and_more"),
        ("appauth", "0006_appusermodel_app_objects"),
        ("auditlog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="logentry",
            name="actor",
        ),
        migrations.AddField(
            model_name="logentry",
            name="platform_actor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="platformauth.platformusermodel",
                verbose_name="platform_actor",
            ),
        ),
        migrations.AddField(
            model_name="logentry",
            name="tenant_actor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="appauth.appusermodel",
                verbose_name="tenant_actor",
            ),
        ),
    ]
