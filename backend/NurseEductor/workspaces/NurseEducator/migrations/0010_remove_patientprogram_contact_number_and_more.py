# Generated by Django 4.2.8 on 2024-01-10 11:10

from django.db import migrations, models
import zelthy.core.storage_utils


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_models', '0009_doctor_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientprogram',
            name='contact_number',
        ),
        migrations.RemoveField(
            model_name='patientprogram',
            name='email',
        ),
        migrations.RemoveField(
            model_name='patientprogram',
            name='prescribing_doctor',
        ),
        migrations.AddField(
            model_name='patient',
            name='consent',
            field=models.BooleanField(default=False, verbose_name='Consent'),
        ),
        migrations.AddField(
            model_name='patientprogram',
            name='consent',
            field=models.BooleanField(default=False, verbose_name='Consent'),
        ),
        migrations.AddField(
            model_name='patientprogram',
            name='consent_date',
            field=models.DateField(blank=True, null=True, verbose_name='Consent Date'),
        ),
        migrations.AddField(
            model_name='patientprogram',
            name='consent_file',
            field=zelthy.core.storage_utils.ZFileField(blank=True, null=True, upload_to=zelthy.core.storage_utils.local_save, validators=[zelthy.core.storage_utils.validate_file_extension]),
        ),
        migrations.AddField(
            model_name='patientprogram',
            name='discontinuation_date',
            field=models.DateField(blank=True, null=True, verbose_name='Discontinuation Date'),
        ),
        migrations.AddField(
            model_name='patientprogram',
            name='discontinuation_reason',
            field=models.CharField(choices=[('dr_decision', "Dr's decision to end treatment"), ('patient_decision', "Patient's decision to end treatment"), ('deceased', 'Deceased'), ('change_medication', 'Change of medication'), ('change_therapy', 'Change of therapy'), ('medication_side_effect', 'Medication side effect'), ('no_response', 'No response to medication'), ('financial_problems', 'Patient financial problems'), ('disease_progression', 'Disease progression'), ('uncontactable', 'Uncontactable'), ('ineligibility_location', 'Program ineligibility (Location)'), ('ineligibility_age', 'Program ineligibility (Age)'), ('ineligibility_employment', 'Program ineligibility (Employment)'), ('ineligibility_citizenship', 'Program ineligibility (Citizenship)'), ('poor_service', 'Poor service/quality of program'), ('opt_out', 'Opt-out from PSP')], default='dr_decision', max_length=20, verbose_name='Contact Person'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patientprogram',
            name='training_date',
            field=models.DateField(blank=True, null=True, verbose_name='Training Date'),
        ),
        migrations.AddField(
            model_name='patientprogram',
            name='training_type',
            field=models.CharField(blank=True, null=True, verbose_name='Training Date'),
        ),
        migrations.AlterField(
            model_name='patientprogram',
            name='contact_person',
            field=models.CharField(choices=[('self', 'Self'), ('spouse', 'Spouse'), ('daughter', 'Daughter'), ('daughter-in-law', 'Daughter-in-law'), ('son', 'Son'), ('son-in-law', 'Son-in-law'), ('nephew', 'Nephew'), ('niece', 'Niece'), ('granddaughter', 'Granddaughter'), ('grandson', 'Grandson'), ('others', 'Others')], max_length=20, verbose_name='Contact Person'),
        ),
    ]
