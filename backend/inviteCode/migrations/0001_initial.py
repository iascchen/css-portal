# Generated by Django 3.0.8 on 2020-07-22 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InviteCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='激活码')),
                ('company', models.CharField(blank=True, max_length=128, verbose_name='公司')),
                ('active', models.BooleanField(default=True, verbose_name='可用')),
                ('users', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Users')),
            ],
            options={
                'verbose_name': 'Users',
            },
        ),
    ]
