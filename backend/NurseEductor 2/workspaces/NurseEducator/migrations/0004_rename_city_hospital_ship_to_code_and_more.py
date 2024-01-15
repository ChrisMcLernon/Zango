# Generated by Django 4.2.8 on 2024-01-06 09:41

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import zelthy.apps.dynamic_models.fields
import zelthy.core.storage_utils


class Migration(migrations.Migration):

    dependencies = [
        ('appauth', '0005_remove_appusermodel_user'),
        ('dynamic_models', '0003_adverseevent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='city',
            new_name='ship_to_code',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='country',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='state',
        ),
        migrations.AddField(
            model_name='hospital',
            name='contact_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Primary Phone'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='address',
            field=models.TextField(max_length=255, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Hospital Name'),
        ),
        migrations.CreateModel(
            name='ProductComplaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('batch_number', models.CharField(max_length=255)),
                ('expiry_date', models.DateField()),
                ('quantity_of_affected_product', models.CharField(max_length=255)),
                ('reported_by', models.CharField(choices=[('hcp', 'HCP'), ('patient', 'Patient'), ('caregiver', 'Caregiver'), ('clinic_staff', 'Clinic staff')], max_length=50)),
                ('clinic_name_address', models.TextField()),
                ('date_of_complaint', models.DateField()),
                ('summary', models.TextField()),
                ('sample_available_for_collection', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('attachment_upload', zelthy.core.storage_utils.ZFileField(upload_to=zelthy.core.storage_utils.local_save, validators=[zelthy.core.storage_utils.validate_file_extension])),
                ('product', models.CharField(choices=[('dupixent_300mg', 'Dupixent 300mg'), ('dupixent_200mg', 'Dupixent 200mg')], max_length=50)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('patient', zelthy.apps.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.patient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NurseEducator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Contact Number')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('user', zelthy.apps.dynamic_models.fields.ZForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appauth.appusermodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NotesTaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('due_date', models.DateField()),
                ('task_type', models.CharField(choices=[('schedule_appointment', 'Schedule appointment'), ('complete_session', 'Complete session'), ('approve_patient', 'Approve patient'), ('approve_doctor', 'Approve Doctor')], max_length=50)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('doctor', zelthy.apps.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.doctor')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('patient', zelthy.apps.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.patient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]