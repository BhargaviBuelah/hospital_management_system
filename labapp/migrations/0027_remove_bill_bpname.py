# Generated by Django 4.1.1 on 2023-02-07 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0026_bill_bpname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='bpname',
        ),
    ]