# Generated by Django 5.1 on 2024-08-24 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_categoy_name_postcategory_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='featured_image',
        ),
    ]
