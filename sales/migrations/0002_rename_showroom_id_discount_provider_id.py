# Generated by Django 4.0.5 on 2022-08-12 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount',
            old_name='showroom_id',
            new_name='provider_id',
        ),
    ]
