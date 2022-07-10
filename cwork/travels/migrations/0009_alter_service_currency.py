# Generated by Django 4.0.5 on 2022-07-10 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0008_service_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='currency',
            field=models.CharField(choices=[('EUR', 'Euro'), ('USD', 'Dollars'), ('RUB', 'Rubles')], default='RUB', max_length=3),
        ),
    ]
