# Generated by Django 4.0.5 on 2022-06-20 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunzapp', '0004_financialneed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]