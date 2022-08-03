# Generated by Django 4.0.6 on 2022-08-01 12:04

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('showroom', '0009_delete_buyer_delete_buyer_history_delete_listofcars_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='buyer',
        ),
        migrations.DeleteModel(
            name='buyer_history',
        ),
        migrations.DeleteModel(
            name='listOfCars',
        ),
        migrations.DeleteModel(
            name='provider',
        ),
        migrations.AlterField(
            model_name='showroom',
            name='location',
            field=django_countries.fields.CountryField(default='RU', max_length=2),
        ),
    ]
