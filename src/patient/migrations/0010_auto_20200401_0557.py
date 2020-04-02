# Generated by Django 2.2.11 on 2020-04-01 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0009_auto_20200331_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('ic_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='applicationforhomecarehomeleave',
            name='name',
        ),
        migrations.AlterField(
            model_name='admission',
            name='full_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_admission', to='patient.Patient'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='ic_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='icnumber_admission', to='patient.Patient'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='full_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='patient.Patient'),
        ),
        migrations.AlterField(
            model_name='cannulation',
            name='full_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_cannulation', to='patient.Patient'),
        ),
        migrations.AlterField(
            model_name='chargessheet',
            name='full_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_chargessheet', to='patient.Patient'),
        ),
        migrations.AddField(
            model_name='applicationforhomecarehomeleave',
            name='full_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='name_homeleave', to='patient.Patient'),
            preserve_default=False,
        ),
    ]
