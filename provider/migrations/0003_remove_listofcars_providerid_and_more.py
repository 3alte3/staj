# Generated by Django 4.0.5 on 2022-08-19 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showroom', '0015_remove_cars_showroom_id_and_more'),
        ('provider', '0002_providerhistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listofcars',
            name='providerId',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='providerId',
        ),
        migrations.RemoveField(
            model_name='providerhistory',
            name='providerId',
        ),
        migrations.RemoveField(
            model_name='providerhistory',
            name='showroom_id',
        ),
        migrations.AddField(
            model_name='listofcars',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='provider.provider'),
        ),
        migrations.AddField(
            model_name='providerhistory',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='provider.provider'),
        ),
        migrations.AddField(
            model_name='providerhistory',
            name='showroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='showroom.showroom'),
        ),
    ]