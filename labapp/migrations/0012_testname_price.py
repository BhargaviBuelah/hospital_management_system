# Generated by Django 4.1.1 on 2023-02-01 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0011_remove_testname_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='testname',
            name='price',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
