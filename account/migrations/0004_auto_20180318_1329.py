# Generated by Django 2.0.3 on 2018-03-18 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20180318_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=15, verbose_name='Telefone de contato'),
        ),
    ]