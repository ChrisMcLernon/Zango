# Generated by Django 4.2.2 on 2023-08-05 13:05

from django.db import migrations, models
import django.db.models.deletion
import zelthy3.backend.apps.tenants.dynamic_models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50, null=True)),
                ('text', models.CharField(max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postalCode', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LandingPageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=20)),
                ('address', zelthy3.backend.apps.tenants.dynamic_models.fields.ZForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.address')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
