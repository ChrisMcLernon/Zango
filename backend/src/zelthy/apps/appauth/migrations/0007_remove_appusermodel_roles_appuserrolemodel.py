# Generated by Django 4.2.10 on 2024-02-12 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appauth', '0006_appusermodel_app_objects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appusermodel',
            name='roles',
        ),
        migrations.CreateModel(
            name='AppUserRoleMappingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app_user_role', to='appauth.userrolemodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app_user', to='appauth.appusermodel')),
            ],
        ),
    ]
