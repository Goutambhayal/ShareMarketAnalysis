# Generated by Django 5.1.1 on 2024-12-19 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intradayData', '0007_alter_intradata_dayhigh_alter_intradata_dayhigh1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='intradata',
            name='Date',
            field=models.DateField(null=True),
        ),
    ]
