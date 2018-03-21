# Generated by Django 2.0.3 on 2018-03-21 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180320_2330'),
        ('buy', '0004_auto_20180321_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item',
        ),
        migrations.AddField(
            model_name='item',
            name='gear',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='item', to='core.Gear', verbose_name='peça'),
            preserve_default=False,
        ),
    ]
