# Generated by Django 5.1.4 on 2025-01-27 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('society_site', '0003_meterrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submeter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomno', models.CharField(max_length=20)),
                ('p', models.IntegerField()),
                ('c', models.IntegerField()),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]
