# Generated by Django 2.2.3 on 2019-07-11 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0008_message_from_fm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='imei',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]