# Generated by Django 4.0.6 on 2022-08-01 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showroom', '0004_showroom_location1_alter_history_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phoneNumber', models.CharField(max_length=255)),
                ('buyerId', models.CharField(max_length=255)),
                ('balance', models.IntegerField()),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='buyer_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyerId', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('showroom_id', models.IntegerField()),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='listOfCars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine_type', models.CharField(max_length=255, null=True)),
                ('max_speed', models.CharField(max_length=255, null=True)),
                ('ammount_of_eng', models.IntegerField(default=0)),
                ('model', models.CharField(max_length=255)),
                ('mark', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('providerId', models.IntegerField()),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.IntegerField()),
                ('ammountOfBuyers', models.IntegerField()),
                ('providerId', models.IntegerField()),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='cars',
            name='ammount_of_eng',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cars',
            name='engine_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cars',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cars',
            name='max_speed',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='charact_showroom',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='history',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='showroom',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='unique_buyers',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='charact_showroom',
            name='engine_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='charact_showroom',
            name='max_speed',
            field=models.CharField(max_length=255, null=True),
        ),
    ]