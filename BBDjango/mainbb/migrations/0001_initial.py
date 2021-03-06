# Generated by Django 3.2.8 on 2021-11-30 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reg_donor_patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('pword', models.CharField(max_length=50)),
                ('fullname', models.CharField(max_length=100)),
                ('add', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('bloodtype', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=4)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('contactnum', models.DecimalField(decimal_places=0, max_digits=11)),
            ],
        ),
    ]