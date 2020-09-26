# Generated by Django 3.1.1 on 2020-09-26 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0005_auto_20200925_2356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Project'},
        ),
        migrations.AlterModelOptions(
            name='projectstudents',
            options={'verbose_name': 'Project Student'},
        ),
        migrations.AlterField(
            model_name='project',
            name='supervisor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='projectstudents',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='project',
            constraint=models.UniqueConstraint(fields=('title', 'supervisor'), name='unique title'),
        ),
        migrations.AddConstraint(
            model_name='projectstudents',
            constraint=models.UniqueConstraint(fields=('student', 'project'), name='unique project student'),
        ),
    ]