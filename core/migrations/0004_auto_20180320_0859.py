# Generated by Django 2.0.3 on 2018-03-20 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_gear_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gear',
            name='thumb',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='core/images'),
        ),
    ]
