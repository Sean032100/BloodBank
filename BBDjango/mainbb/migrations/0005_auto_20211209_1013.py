# Generated by Django 3.2.8 on 2021-12-09 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbb', '0004_auto_20211207_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_reqblood',
            name='date_request',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='add_reqdonate',
            name='date_request',
            field=models.DateField(null=True),
        ),
    ]