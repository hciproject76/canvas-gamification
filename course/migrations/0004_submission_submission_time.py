# Generated by Django 3.0.1 on 2020-02-17 09:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20200217_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='submission_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
