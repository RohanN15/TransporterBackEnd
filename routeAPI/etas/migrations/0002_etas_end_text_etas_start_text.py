# Generated by Django 4.2.7 on 2023-12-08 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='etas',
            name='end_text',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='etas',
            name='start_text',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
