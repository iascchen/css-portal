# Generated by Django 3.0.8 on 2020-08-05 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_users_phone'),
        ('inviteCode', '0003_auto_20200803_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitecode',
            name='creater',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invitecode_creater', to='users.Users'),
        ),
    ]
