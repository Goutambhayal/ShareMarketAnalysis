# Generated by Django 5.1.1 on 2024-12-16 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intradayData', '0003_intradata_finalgain1'),
    ]

    operations = [
        migrations.AddField(
            model_name='intradata',
            name='finalGain2',
            field=models.FloatField(null=True),
        ),
    ]