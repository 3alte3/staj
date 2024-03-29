# Generated by Django 4.0.6 on 2022-08-02 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0003_alter_buyer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='buyer',
            name='password',
            field=models.CharField(default=0, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
