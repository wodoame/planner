# Generated by Django 4.2.2 on 2023-10-25 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_label_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='theme',
            field=models.CharField(choices=[('theme-1', 'blue theme'), ('theme-2', 'purple theme'), ('theme-3', 'orange theme'), ('theme-4', 'green theme')], max_length=128, null=True),
        ),
    ]
