# Generated by Django 2.1.5 on 2019-02-06 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seminarsession',
            name='seminar_token',
            field=models.CharField(default='dxyxxxxsjakj', max_length=64),
        ),
    ]
