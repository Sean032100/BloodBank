# Generated by Django 3.2.8 on 2021-12-06 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbb', '0003_auto_20211130_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_reqblood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('patientname', models.CharField(max_length=100)),
                ('patientage', models.DecimalField(decimal_places=0, max_digits=3)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('healthfac', models.CharField(max_length=200)),
                ('healthfacadd', models.CharField(max_length=200)),
                ('contactnum', models.DecimalField(decimal_places=0, max_digits=11)),
                ('disease', models.CharField(max_length=100)),
                ('unit', models.DecimalField(decimal_places=0, max_digits=3)),
                ('bloodtype', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=4)),
                ('status', models.CharField(choices=[('Request Sent', 'Request Sent')], max_length=20)),
                ('remarks', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='add_reqdonate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('fullname', models.CharField(max_length=100)),
                ('age', models.DecimalField(decimal_places=0, max_digits=3)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('add', models.CharField(max_length=200)),
                ('contactnum', models.DecimalField(decimal_places=0, max_digits=11)),
                ('weight', models.DecimalField(decimal_places=0, max_digits=3)),
                ('disease', models.CharField(max_length=100)),
                ('unit', models.DecimalField(decimal_places=0, max_digits=3)),
                ('bloodtype', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=4)),
                ('status', models.CharField(choices=[('Request Sent', 'Request Sent')], max_length=20)),
                ('remarks', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='reg_donor_patient',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reg_donor_patient',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
    ]
