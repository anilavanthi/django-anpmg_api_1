# Generated by Django 4.0.4 on 2023-07-22 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Masters', '0038_customer_dateofdeath_customer_dateofmarriagewidowed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='nameofappfilling',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='nameofappmobile',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='nameofapprelation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
