# Generated by Django 3.2.6 on 2021-10-15 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rollindustries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
