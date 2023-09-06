# Generated by Django 4.2.4 on 2023-09-06 09:46

from django.db import migrations, models
import django.db.models.deletion
import zelthy.apps.dynamic_models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_models', '0030_patientbenefitmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='patient_benefit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='all_benefit_orders', to='dynamic_models.patientbenefitmodel'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='city_fk',
            field=zelthy.apps.dynamic_models.fields.ZForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.citymodel'),
        ),
    ]
