# Generated by Django 2.1.5 on 2019-02-04 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blip_core', '0002_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_time_date',
            field=models.DateTimeField(),
        ),
    ]
