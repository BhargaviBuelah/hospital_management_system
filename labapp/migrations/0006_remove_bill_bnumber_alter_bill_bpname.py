# Generated by Django 4.1.1 on 2023-01-31 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0005_bill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='bnumber',
        ),
        migrations.AlterField(
            model_name='bill',
            name='bpname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labapp.patient'),
        ),
    ]
