# Generated by Django 4.0.1 on 2022-10-03 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cnnresult',
            name='hr',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='cnnresult',
            name='qc',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='cnnresult',
            name='qi',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='cnnresult',
            name='td',
            field=models.FloatField(),
        ),
    ]
