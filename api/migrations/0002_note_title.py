# Generated by Django 4.1 on 2022-08-23 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
