# Generated by Django 4.1.1 on 2022-09-22 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_alter_task_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='No title', max_length=100, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=500, null=True, verbose_name='Описание'),
        ),
    ]
