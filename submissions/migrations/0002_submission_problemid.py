# Generated by Django 2.2.4 on 2019-08-09 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='problemid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
