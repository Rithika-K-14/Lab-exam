# Generated by Django 3.1.4 on 2022-12-07 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainticket',
            old_name='content',
            new_name='Name',
        ),
        migrations.AddField(
            model_name='trainticket',
            name='from1',
            field=models.CharField(default='CityA', max_length=20),
        ),
        migrations.AddField(
            model_name='trainticket',
            name='to1',
            field=models.CharField(default='CityA', max_length=20),
        ),
    ]
