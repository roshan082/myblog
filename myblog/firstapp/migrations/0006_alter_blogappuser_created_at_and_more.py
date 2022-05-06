# Generated by Django 4.0.4 on 2022-05-05 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_alter_blogappuser_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogappuser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 17, 4, 15, 295933)),
        ),
        migrations.AlterField(
            model_name='blogappuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='blogappuser',
            name='is_removed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blogappuser',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blogappuser',
            name='verification_code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 17, 4, 15, 296966)),
        ),
    ]
