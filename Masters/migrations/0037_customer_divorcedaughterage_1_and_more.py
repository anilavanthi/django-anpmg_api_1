# Generated by Django 4.0.4 on 2023-07-22 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Masters', '0036_alter_customer_religion'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='divorceDaughterAge_1',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='divorceDaughterAge_2',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='divorceDaughterAge_3',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='divorceDaughterAge_4',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='divorceDaughterMStatus_1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='divorceDaughterMStatus_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='divorceDaughterMStatus_3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='divorceDaughterMStatus_4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='divorceDaughterName_1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='divorceDaughterName_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='divorceDaughterName_3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='divorceDaughterName_4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='divorcenoofdaughters',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
