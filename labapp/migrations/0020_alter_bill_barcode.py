# Generated by Django 4.1.1 on 2023-02-06 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0019_alter_bill_barcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='barcode',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
