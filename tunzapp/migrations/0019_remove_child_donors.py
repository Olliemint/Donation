# Generated by Django 4.0.5 on 2022-06-23 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tunzapp', '0018_child_donors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='donors',
        ),
    ]
