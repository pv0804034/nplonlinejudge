# Generated by Django 2.2.4 on 2019-08-09 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problemsets', '0002_auto_20190805_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='attempts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='problem',
            name='successes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='problem',
            name='memorylimit',
            field=models.IntegerField(default=256),
        ),
        migrations.AlterField(
            model_name='problem',
            name='statement',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='problem',
            name='timelimit',
            field=models.IntegerField(default=1000),
        ),
    ]
