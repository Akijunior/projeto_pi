# Generated by Django 2.0.3 on 2018-03-20 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20180318_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_data',
            field=models.DateField(blank=True, null=True, verbose_name='Data de nascimento'),
        ),
    ]