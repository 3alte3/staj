# Generated by Django 4.0.5 on 2022-08-19 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0006_remove_buyer_buyerid_remove_buyer_history_buyerid_and_more'),
        ('showroom', '0015_remove_cars_showroom_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buyer.buyer'),
        ),
    ]