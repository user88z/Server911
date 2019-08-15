# Generated by Django 2.2.3 on 2019-07-10 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0004_auto_20190710_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='GPS_speed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='GSM_dBm',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='battery_level',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='date_to_end',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='motion_T',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='motion_TS',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='temperature',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='time_GPS_search',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='time_GSM_registration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
