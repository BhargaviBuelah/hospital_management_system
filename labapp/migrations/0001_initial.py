# Generated by Django 4.1.1 on 2023-01-28 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('pdesc', models.CharField(max_length=150)),
                ('dname', models.CharField(max_length=100)),
                ('test', models.CharField(max_length=100)),
                ('is_deleted', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Testname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=100)),
            ],
        ),
    ]
