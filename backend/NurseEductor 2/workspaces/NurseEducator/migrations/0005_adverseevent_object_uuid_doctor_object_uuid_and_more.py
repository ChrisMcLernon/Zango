# Generated by Django 4.2.8 on 2024-01-06 10:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_models', '0004_rename_city_hospital_ship_to_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adverseevent',
            name='object_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='object_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='object_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='notestaskmodel',
            name='object_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='nurseeducator',
            name='object_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='object_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='patientprogram',
            name='object_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='productcomplaints',
            name='object_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]