# Generated by Django 3.2.6 on 2022-05-12 11:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_new_device_baud_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='new_device',
            name='Gateway_Name',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]