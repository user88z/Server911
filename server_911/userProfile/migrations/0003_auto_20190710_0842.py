# Generated by Django 2.2.3 on 2019-07-10 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0002_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='enable_SearchMode',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='device',
            name='enable_acс',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='device',
            name='motion',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='device',
            name='send_SMS_MoveAcc',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='device',
            name='send_SMS_SearchMode',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='device',
            name='send_data_Email',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='device',
            name='send_status_30days',
            field=models.BooleanField(default=False),
        ),
    ]