# Generated by Django 3.1 on 2021-04-05 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_awsdescribe', '0008_auto_20210318_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpAddress',
            fields=[
                ('ip', models.GenericIPAddressField(primary_key=True, serialize=False)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Sg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vpc_id', models.CharField(max_length=50)),
                ('sg_tags', models.TextField()),
                ('ip_permissions', models.TextField()),
                ('ip_permissions_egress', models.TextField()),
                ('group_id', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('group_name', models.CharField(max_length=255)),
                ('ae_index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_awsdescribe.awsenvironment')),
            ],
        ),
    ]
