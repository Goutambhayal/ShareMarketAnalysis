# Generated by Django 5.1.1 on 2024-12-16 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intradayData', '0002_alter_intradata_companyname'),
    ]

    operations = [
        migrations.AddField(
            model_name='intradata',
            name='finalGain1',
            field=models.FloatField(null=True),
        ),
    ]