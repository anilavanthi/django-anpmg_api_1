# Generated by Django 4.0.4 on 2023-07-18 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Masters', '0033_customer_fatheraddress_customer_fatherannualincome_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='motherAddress',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='motherAnnualIncome',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='motherHealth',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='motherMobile',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='motherPension',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='motherProfession',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='motherProperty',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='motherWSector',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]