# Generated by Django 4.0.5 on 2022-07-09 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0004_alter_service_offers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='offers',
        ),
    ]