# Generated by Django 3.1.2 on 2020-11-20 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shaad', '0002_auto_20201120_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.TextField(null=True),
        ),
    ]