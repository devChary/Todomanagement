# Generated by Django 3.0.3 on 2020-02-21 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_todo_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]
