# Generated by Django 3.1.1 on 2020-10-06 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_auto_20200930_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='dueDate',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='task',
            name='dueTime',
            field=models.TimeField(default=None),
        ),
        migrations.AddField(
            model_name='task',
            name='startDate',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='task',
            name='startTime',
            field=models.TimeField(default=None),
        ),
        migrations.AlterField(
            model_name='task',
            name='sourceproject',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
    ]