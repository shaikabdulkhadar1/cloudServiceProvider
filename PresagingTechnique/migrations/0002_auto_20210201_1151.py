# Generated by Django 2.0.8 on 2021-02-01 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PresagingTechnique', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerregistrationmodel',
            name='address',
            field=models.CharField(max_length=1000),
        ),
    ]