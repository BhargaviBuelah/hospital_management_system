# Generated by Django 4.1.1 on 2023-01-30 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0003_remove_patient_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='pid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testname',
            name='tid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
