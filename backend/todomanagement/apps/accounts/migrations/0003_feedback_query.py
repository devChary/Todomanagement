# Generated by Django 3.0.3 on 2020-02-22 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='query',
            field=models.TextField(blank=True, null=True, verbose_name='Query'),
        ),
    ]
