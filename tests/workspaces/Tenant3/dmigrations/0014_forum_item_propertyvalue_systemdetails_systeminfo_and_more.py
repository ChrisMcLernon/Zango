# Generated by Django 4.2.3 on 2023-08-09 10:05

from django.db import migrations, models
import django.db.models.deletion
import zelthy3.backend.apps.tenants.dynamic_models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_models', '0013_delete_d'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forum_name', models.CharField(max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PropertyValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SystemDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SystemInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_name', models.CharField(max_length=32)),
                ('system_details', zelthy3.backend.apps.tenants.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.systemdetails')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('item', zelthy3.backend.apps.tenants.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='props', to='dynamic_models.item')),
                ('value', zelthy3.backend.apps.tenants.dynamic_models.fields.ZForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dynamic_models.propertyvalue')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('forum', zelthy3.backend.apps.tenants.dynamic_models.fields.ZForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dynamic_models.forum')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='forum',
            name='system_info',
            field=zelthy3.backend.apps.tenants.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.systeminfo'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=250)),
                ('post', zelthy3.backend.apps.tenants.dynamic_models.fields.ZForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dynamic_models.npost')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]