# Generated by Django 2.2.4 on 2019-08-09 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default='Nepal', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(default='About myself', max_length=1000),
        ),
    ]