# Generated by Django 4.0.5 on 2022-06-20 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunzapp', '0010_remove_child_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialneed',
            name='needs',
            field=models.CharField(default='School Fees', max_length=50, unique=True),
        ),
    ]
