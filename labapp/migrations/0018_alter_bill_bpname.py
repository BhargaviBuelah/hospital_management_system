# Generated by Django 4.1.1 on 2023-02-04 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0017_alter_bill_bpname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bpname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labapp.patient'),
        ),
    ]
