# Generated by Django 2.2.6 on 2019-11-02 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tierstats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tierstat',
            name='aggregate_percent',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
        migrations.AlterField(
            model_name='tierstat',
            name='summoner_percent',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
    ]
