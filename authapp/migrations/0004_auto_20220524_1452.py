# Generated by Django 3.2.6 on 2022-05-24 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_monophase_triphase_vfd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monophase',
            name='Adress',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='monophase',
            name='Monophase_Time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='triphase',
            name='Adress',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='triphase',
            name='Triphase_Time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='Adress',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='VFD_Time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='c00',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='c01',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='c02',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='c03',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='c04',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='c06',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='c07',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='c12',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='c13',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='c14',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='c15',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='c16',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='c17',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='c18',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='c19',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='c20',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='c21',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='c23',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='c24',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='c25',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vfd',
            name='c27',
            field=models.FloatField(),
        ),
    ]
