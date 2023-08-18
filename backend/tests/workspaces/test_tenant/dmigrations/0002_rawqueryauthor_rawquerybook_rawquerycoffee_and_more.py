# Generated by Django 4.2.3 on 2023-08-18 08:30

from django.db import migrations, models
import django.db.models.deletion
import zelthy.apps.dynamic_models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawQueryAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RawQueryBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('paperback', models.BooleanField(default=False)),
                ('opening_line', models.TextField()),
                ('author', zelthy.apps.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.rawqueryauthor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RawQueryCoffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(db_column='name', max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RawQueryMixedCaseIDColumn',
            fields=[
                ('id', models.AutoField(db_column='MiXeD_CaSe_Id', primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RawQueryBookFkAsPk',
            fields=[
                ('book', zelthy.apps.dynamic_models.fields.ZForeignKey(db_column='not_the_default', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dynamic_models.rawquerybook')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
