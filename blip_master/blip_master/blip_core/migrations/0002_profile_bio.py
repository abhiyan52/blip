# Generated by Django 2.1.5 on 2019-02-04 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blip_core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='This is default bio', max_length=500),
        ),
    ]
