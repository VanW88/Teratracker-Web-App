# Generated by Django 3.1 on 2020-09-26 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20200927_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskdesc',
            field=models.TextField(max_length=500),
        ),
    ]