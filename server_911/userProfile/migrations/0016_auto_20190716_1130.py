# Generated by Django 2.2.3 on 2019-07-16 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0015_auto_20190716_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='GPS_speed',
            field=models.CharField(blank=True, default=0, max_length=8),
            preserve_default=False,
        ),
    ]
