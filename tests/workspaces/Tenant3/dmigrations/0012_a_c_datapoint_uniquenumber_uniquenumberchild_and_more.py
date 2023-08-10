# Generated by Django 4.2.3 on 2023-08-09 09:38

from django.db import migrations, models
import django.db.models.deletion
import zelthy3.backend.apps.tenants.dynamic_models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_models', '0011_remove_child1_parent1_ptr_remove_child1_parent2_ptr_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField(default=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='C',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('y', models.IntegerField(default=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=20)),
                ('another_value', models.CharField(blank=True, max_length=20)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UniqueNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UniqueNumberChild',
            fields=[
                ('uniquenumber_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dynamic_models.uniquenumber')),
            ],
            options={
                'abstract': False,
            },
            bases=('dynamic_models.uniquenumber',),
        ),
        migrations.CreateModel(
            name='RelatedPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('data', zelthy3.backend.apps.tenants.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.datapoint')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='B',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('y', models.IntegerField(default=10)),
                ('a', zelthy3.backend.apps.tenants.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.a')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='D',
            fields=[
                ('c_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dynamic_models.c')),
                ('a', zelthy3.backend.apps.tenants.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.a')),
            ],
            options={
                'abstract': False,
            },
            bases=('dynamic_models.c',),
        ),
    ]