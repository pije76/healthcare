# Generated by Django 2.2.11 on 2020-03-31 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_auto_20200330_0804'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('ic_number', models.CharField(max_length=100)),
                ('date_time_of_appointment', models.CharField(max_length=100)),
                ('hospital_clinic', models.CharField(max_length=100)),
                ('treatment_order', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='admission',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=100),
        ),
        migrations.AlterField(
            model_name='admission',
            name='mode',
            field=models.CharField(choices=[('ambulance', 'Ambulance'), ('own', 'Own Transport')], max_length=100),
        ),
    ]
