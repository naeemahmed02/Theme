# Generated by Django 5.1 on 2024-08-23 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_aboutus'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
