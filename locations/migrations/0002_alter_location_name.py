# Generated by Django 3.2.24 on 2024-03-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]