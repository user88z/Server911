# Generated by Django 2.2.3 on 2019-07-11 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0009_auto_20190711_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='launch_period',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
