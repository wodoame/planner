# Generated by Django 4.2.2 on 2023-10-30 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_task_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['date_created']},
        ),
    ]
