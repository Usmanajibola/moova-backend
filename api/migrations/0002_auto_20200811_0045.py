# Generated by Django 3.0.9 on 2020-08-11 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='nickname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='phone_number',
            field=models.CharField(max_length=50),
        ),
    ]
