# Generated by Django 4.2.8 on 2024-01-10 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_models', '0010_remove_patientprogram_contact_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='consent',
            field=models.BooleanField(default=False, verbose_name='Consent'),
        ),
        migrations.AlterField(
            model_name='patientprogram',
            name='discontinuation_reason',
            field=models.CharField(blank=True, choices=[('dr_decision', "Dr's decision to end treatment"), ('patient_decision', "Patient's decision to end treatment"), ('deceased', 'Deceased'), ('change_medication', 'Change of medication'), ('change_therapy', 'Change of therapy'), ('medication_side_effect', 'Medication side effect'), ('no_response', 'No response to medication'), ('financial_problems', 'Patient financial problems'), ('disease_progression', 'Disease progression'), ('uncontactable', 'Uncontactable'), ('ineligibility_location', 'Program ineligibility (Location)'), ('ineligibility_age', 'Program ineligibility (Age)'), ('ineligibility_employment', 'Program ineligibility (Employment)'), ('ineligibility_citizenship', 'Program ineligibility (Citizenship)'), ('poor_service', 'Poor service/quality of program'), ('opt_out', 'Opt-out from PSP')], max_length=20, null=True, verbose_name='Discontinuation Reason'),
        ),
    ]
