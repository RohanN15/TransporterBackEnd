# Generated by Django 4.2.8 on 2023-12-09 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etas', '0002_etas_end_text_etas_start_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='etas',
            name='time_text',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
