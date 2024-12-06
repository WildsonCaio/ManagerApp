# Generated by Django 5.1.3 on 2024-12-05 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_project_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='task',
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pendng'), ('IN_EXECUTION', 'In Execution'), ('COMPLETED', 'Completed')], default='OPEN', max_length=15),
        ),
    ]