# Generated by Django 4.0.5 on 2022-06-23 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tunzapp', '0015_financialneed_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='name',
        ),
    ]