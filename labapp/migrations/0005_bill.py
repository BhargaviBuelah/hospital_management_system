# Generated by Django 4.1.1 on 2023-01-30 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0004_patient_pid_testname_tid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bpname', models.CharField(max_length=100)),
                ('bnumber', models.CharField(max_length=20)),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labapp.tests')),
                ('test_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labapp.testname')),
            ],
        ),
    ]
