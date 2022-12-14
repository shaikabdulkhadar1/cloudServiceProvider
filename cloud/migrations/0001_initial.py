# Generated by Django 2.0.13 on 2020-07-02 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CspRegisterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('loginid', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('locality', models.CharField(max_length=100)),
                ('service', models.CharField(max_length=100)),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField()),
            ],
            options={
                'db_table': 'CspUsers',
            },
        ),
    ]
