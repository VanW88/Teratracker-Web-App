# Generated by Django 3.1.1 on 2020-09-29 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_auto_20200930_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskstudents',
            name='time',
            field=models.IntegerField(default=0),
        ),
    ]