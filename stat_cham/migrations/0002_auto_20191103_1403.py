# Generated by Django 2.2.6 on 2019-11-03 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stat_cham', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stat_champions',
            old_name='cs_avg',
            new_name='cs_average',
        ),
        migrations.RenameField(
            model_name='stat_champions',
            old_name='gold_avg',
            new_name='gold_average',
        ),
    ]